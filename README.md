# End-to-End AWS Data Engineering Project

## Business Use Case
Built an analytics platform for an e-commerce business to analyze customer behavior, product performance, and revenue trends.

## Architecture
- Python for ingestion and transformation
- Amazon S3 as a data lake (raw & processed layers)
- Amazon Redshift Serverless as a data warehouse
- SQL for analytics

## Data Pipeline
1. Ingest raw CSV data into S3
2. Transform data into star schema (dim & fact tables)
3. Upload processed data to S3
4. Load data into Redshift using COPY
5. Run analytical SQL queries

## Technologies Used
- Python (Pandas, Boto3)
- AWS S3
- AWS Redshift Serverless
- SQL
- Git/GitHub

## Sample Analytics
- Monthly revenue trends
- Top-performing product categories
- Customer-level revenue analysis

