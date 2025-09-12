# AWS Data Pipeline Project

## 🧰 Services Used
- Amazon S3
- AWS Glue (Crawler + ETL Job)
- Amazon Athena

## 📊 Objective
Build a serverless data pipeline that ingests raw data into S3, transforms it using AWS Glue, and queries it using Athena.

## 🗂️ Folder Structure
- `data/`: Sample raw data
- `glue_jobs/`: ETL scripts
- `athena_queries/`: SQL queries
- `docs/`: Setup and usage guides

## 🧱 Architecture Overview
![Architecture Diagram](architecture_diagram.png)

## 🚀 How to Run
1. Upload raw data to S3
2. Run Glue Crawler to catalog data
3. Execute Glue ETL job
4. Query processed data with Athena

## 📈 Future Enhancements
- Add QuickSight dashboards
- Automate pipeline with Lambda + CloudWatch
