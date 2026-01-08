import os
import logging
import pandas as pd

# ---------------- CONFIG ---------------- #
RAW_DATA_PATH = "C:/Users/marel/OneDrive/SUMMER 2023/MACHINE LEARNING/PROJECT/E-Commerce Data Engineering Project/Brazilian E-Commerce Public Dataset by Olist/ecommerce-data"
OUTPUT_PATH = "../transformed-data"

os.makedirs(OUTPUT_PATH, exist_ok=True)

# ---------------- LOGGING ---------------- #
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def load_csv(file_name):
    return pd.read_csv(os.path.join(RAW_DATA_PATH, file_name))

def main():
    logging.info("Loading raw data")

    customers = load_csv("customers.csv")
    orders = load_csv("orders.csv")
    order_items = load_csv("order_items.csv")
    products = load_csv("products.csv")

    logging.info("Cleaning data")
    customers.drop_duplicates(inplace=True)
    orders.drop_duplicates(inplace=True)

    logging.info("Creating dimension tables")

    dim_customers = customers[[
        "customer_id", "customer_city", "customer_state"
    ]].drop_duplicates()

    dim_products = products[[
        "product_id", "product_category_name"
    ]].drop_duplicates()

    logging.info("Creating fact table")

    fact_orders = (
        order_items
        .merge(orders, on="order_id")
        .merge(products, on="product_id")
    )

    fact_orders["revenue"] = fact_orders["price"] + fact_orders["freight_value"]

    logging.info("Writing transformed data")

    dim_customers.to_csv(f"C:/Users/marel/Downloads/end-to-end-aws-data-engineering/transformed-data/dim_customers.csv", index=False)
    dim_products.to_csv(f"C:/Users/marel/Downloads/end-to-end-aws-data-engineering/transformed-data/dim_products.csv", index=False)
    fact_orders.to_csv(f"C:/Users/marel/Downloads/end-to-end-aws-data-engineering/transformed-data/fact_orders.csv", index=False)

    logging.info("Transformation completed successfully")

if __name__ == "__main__":
    main()

