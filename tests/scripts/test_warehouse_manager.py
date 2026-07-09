print("File Started")

import pandas as pd

from src.warehouse.warehouse_manager import WarehouseManager


def main():
    print("Inside main()")

    customers_df = pd.read_parquet("data/silver/customers.parquet")

    manager = WarehouseManager("data/gold")

    manager.build_customer_dimension(customers_df)

    print("Completed Successfully")


if __name__ == "__main__":
    print("Calling main()")
    main()