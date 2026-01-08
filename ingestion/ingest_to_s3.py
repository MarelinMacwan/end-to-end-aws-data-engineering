import os
import logging
import boto3
import pandas as pd

# ---------- CONFIG ----------
LOCAL_DATA_PATH = "C:/Users/marel/OneDrive/SUMMER 2023/MACHINE LEARNING/PROJECT/E-Commerce Data Engineering Project/Brazilian E-Commerce Public Dataset by Olist/ecommerce-data"
S3_BUCKET = "ecommerce-data-lake-aws"
S3_PREFIX = "raw"

FILES = {
    "customers": "customers.csv",
    "orders": "orders.csv",
    "order_items": "order_items.csv",
    "products": "products.csv",
    "payments": "payments.csv"
}

# ---------- LOGGING ----------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ---------- S3 CLIENT ----------
s3 = boto3.client("s3")


def upload_to_s3(local_file, s3_key):
    s3.upload_file(local_file, S3_BUCKET, s3_key)
    logging.info(f"Uploaded to s3://{S3_BUCKET}/{s3_key}")


def ingest_file(table_name, file_name):
    file_path = os.path.join(LOCAL_DATA_PATH, file_name)

    logging.info(f"Reading {table_name} data")
    df = pd.read_csv(file_path)

    logging.info(f"{table_name} row count: {len(df)}")

    s3_key = f"{S3_PREFIX}/{table_name}/{file_name}"
    upload_to_s3(file_path, s3_key)


def main():
    for table, file in FILES.items():
        ingest_file(table, file)

    logging.info("Data ingestion completed successfully")


if __name__ == "__main__":
    main()

