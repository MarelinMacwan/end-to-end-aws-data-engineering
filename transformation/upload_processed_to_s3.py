import logging
import boto3
from pathlib import Path
from botocore.exceptions import ClientError

# ---------------- CONFIG ---------------- #
BASE_DIR = Path(__file__).resolve().parent.parent
PROCESSED_DATA_PATH = BASE_DIR / "transformed-data"

S3_BUCKET = "ecommerce-data-lake-aws"   # change if needed
S3_PREFIX = "processed"

FILES = {
    "dim_customers": "dim_customers.csv",
    "dim_products": "dim_products.csv",
    "fact_orders": "fact_orders.csv"
}

# ---------------- LOGGING ---------------- #
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

s3 = boto3.client("s3")


def upload_file(local_path: Path, s3_key: str):
    try:
        s3.upload_file(str(local_path), S3_BUCKET, s3_key)
        logging.info(f"Uploaded to s3://{S3_BUCKET}/{s3_key}")
    except ClientError as e:
        logging.error(f"Upload failed: {e}")
        raise


def main():
    for table, file_name in FILES.items():
        local_file = PROCESSED_DATA_PATH / file_name
        s3_key = f"{S3_PREFIX}/{table}/{file_name}"
        upload_file(local_file, s3_key)

    logging.info("Processed data uploaded successfully")


if __name__ == "__main__":
    main()
