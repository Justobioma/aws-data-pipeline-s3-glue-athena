import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

# Initialize contexts
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Parameters
source_database = "contacts-db"
source_table = "raw"
output_path = "s3://your-bucket-name/processed/"

# Load raw data from Glue Catalog
datasource = glueContext.create_dynamic_frame.from_catalog(
    database=source_database,
    table_name=source_table
)

# Transform: Filter rows where age > 30
filtered_data = Filter.apply(datasource, lambda row: row["age"] > 30)

# Write to S3 in Parquet format
glueContext.write_dynamic_frame.from_options(
    frame=filtered_data,
    connection_type="s3",
    connection_options={"path": output_path},
    format="parquet"
)

job.commit()