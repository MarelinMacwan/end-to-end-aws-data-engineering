import pandas as pd
from great_expectations.dataset import PandasDataset
import sys


class CustomersDataset(PandasDataset):
    _expectation_suite_name = "customers_expectations"

    
class OrdersDataset(PandasDataset):
    _expectation_suite_name = "orders_expectations"


def validate_customers():
    df = pd.read_csv("C:\\Users\\marel\\Downloads\\end-to-end-aws-data-engineering\\transformed-data\\dim_customers.csv")
    ge_df = CustomersDataset(df)

    ge_df.expect_column_values_to_not_be_null("customer_id")
    ge_df.expect_column_values_to_be_unique("customer_id")
    
    return ge_df.validate()


def validate_orders():
    df = pd.read_csv("C:\\Users\\marel\\Downloads\\end-to-end-aws-data-engineering\\transformed-data\\fact_orders.csv")
    ge_df = OrdersDataset(df)

    ge_df.expect_column_values_to_not_be_null("order_id")
    ge_df.expect_column_values_to_be_unique("order_id")
    ge_df.expect_column_values_to_be_between("revenue", min_value=0)

    return ge_df.validate()


if __name__ == "__main__":
    customer_result = validate_customers()
    order_result = validate_orders()

    if not customer_result["success"] or not order_result["success"]:
        print("❌ Data quality checks failed")
        sys.exit(1)

    print("✅ All data quality checks passed")
