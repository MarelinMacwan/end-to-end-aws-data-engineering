# End-to-End AWS Data Engineering Project

## Project Overview
This project demonstrates a complete end-to-end AWS data engineering workflow for an e-commerce analytics platform. It leverages cloud-native services and modern data engineering practices to ingest, transform, store, and analyze e-commerce data at scale.

The workflow is built using the **Brazilian E-commerce Dataset from Kaggle** and is designed to provide actionable business insights such as revenue trends, top-performing products, and customer-level revenue analysis.

---

## Architecture

![ChatGPT Image Jan 10, 2026, 08_29_13 PM](https://github.com/user-attachments/assets/396679d5-042f-410e-a98c-3c35216866ca)

The architecture uses a **data lake and data warehouse pattern**:

- **Data Ingestion:** Python scripts (Pandas, Boto3) extract raw CSV files and upload them to Amazon S3.  
- **Data Lake (S3):** Data is stored in raw and processed layers, allowing versioning and reprocessing if needed.  
- **Data Transformation:** Raw data is transformed into a **star schema** to optimize analytics performance.  
- **Data Warehouse (Redshift Serverless):** Processed data is loaded using `COPY` commands, enabling fast and scalable SQL queries.  
- **Analytics & Reporting:** SQL queries are executed on Redshift to extract insights, including monthly revenue trends, top product categories, and customer revenue metrics.  
- **Version Control:** Git/GitHub is used for workflow management, code versioning, and reproducibility.  

**Data Flow:**  
Python → Raw S3 → Processed S3 → Redshift → SQL Analytics

---

## Technologies Used
- **Python:** Pandas, Boto3 for data ingestion and transformation  
- **AWS S3:** Raw and processed data lake layers  
- **AWS Redshift Serverless:** Data warehouse for analytics  
- **SQL:** For querying and reporting  
- **Git/GitHub:** Version control and project management  

---

## Key Highlights
- Designed to handle large-scale e-commerce datasets efficiently  
- Implements a modular, reusable, and scalable data pipeline architecture  
- Demonstrates full cloud data engineering lifecycle from ingestion to analytics  
- Integrates real-world dataset: Brazilian E-commerce Dataset from Kaggle  

---

## Sample Analytics
- **Monthly Revenue Trends:** Track revenue growth over time  
- **Top Product Categories:** Identify high-performing products  
- **Customer Revenue Analysis:** Segment customers based on purchase behavior

