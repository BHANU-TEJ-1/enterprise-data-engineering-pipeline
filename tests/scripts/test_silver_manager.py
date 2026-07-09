import pandas as pd

from src.bronze.bronze_layer import BronzeLayer
from src.silver.silver_manager import SilverManager


def main():

    # ------------------------------------
    # Create Sample Bronze Data
    # ------------------------------------

    df = pd.DataFrame(
        {
            " Customer Name ": [
                " john ",
                "Alice",
                "Alice",
            ],
            "Age": [
                "25",
                "30",
                "30",
            ],
            "City": [
                " new york ",
                "LONDON",
                "LONDON",
            ],
            "Order-Date": [
                "2024/01/01",
                "2024/02/01",
                "2024/02/01",
            ],
        }
    )

    bronze = BronzeLayer()

    bronze.write(
        df,
        "customers_test",
    )

    # ------------------------------------
    # Silver Manager
    # ------------------------------------

    manager = SilverManager()

    cleaning_config = {
        "trim_whitespace": True,
        "replace_empty": True,
        "drop_empty_rows": True,
        "fill_missing": False,
    }

    standardization_config = {
        "text_columns": [
            "customer_name",
            "city",
        ],
        "date_columns": [
            "order_date",
        ],
    }

    deduplication_config = {
        "subset": [
            "customer_name",
            "age",
        ],
        "keep": "first",
    }

    schema = {
        "age": "int",
        "order_date": "datetime",
    }

    output = manager.process(
        bronze_path="data/bronze/customers_test.parquet",
        table_name="customers",
        cleaning_config=cleaning_config,
        standardization_config=standardization_config,
        deduplication_config=deduplication_config,
        schema=schema,
    )

    print("\nSilver Output")
    print(output)


if __name__ == "__main__":
    main()