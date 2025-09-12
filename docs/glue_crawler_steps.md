Steps to Create Glue Crawler
Pre requisites:
1. AWS Account
2. Access to AWS Glue
3. AWS S3 buckets with preloaded CSV data(preferably in a drectory)

Whilst signed into AWS, Go to AWS Glue and click on "Crawlers"
1. Name your "Crawler"
2. Choose a data store ie where the Crawler should look for the data file. This would be your S3 bucket or folder
3. Add the necessar permissions. This would an IAM role with a prefix of "AWSGlueServiceRole-". You can add your preferred extension
4. Choose an "on-demand" frequency for the schedule
5. Next, create a database for the Crawler. This is quite easy to set up
6. After reviewing all the selections, Create Crawler to finalise.

***RUNNING the Crawler**
This involesthe process of Glue executing the Crawler after it is created. Just click on "Run Crawler"
You can view AWS Glue Data Catalog objects after you have run the Crawler. These objects include the Glue database, tables and the schemas.
