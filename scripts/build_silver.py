"""
build_silver.py

Build the complete Silver Layer.
"""

from src.silver.silver_manager import SilverManager


def build_silver():

    manager = SilverManager()

    cleaning_config = {
        "trim_whitespace": True,
        "replace_empty": True,
        "drop_empty_rows": True,
        "fill_missing": False,
    }

    standardization_config = {
        "text_columns": [],
        "date_columns": [],
    }

    deduplication_config = {
        "subset": None,
        "keep": "first",
    }

    schema = {}

    tables = [
        "customers",
        "geolocation",
        "orders",
        "order_items",
        "products",
        "category_translation",
        "payments",
        "sellers",
        "reviews",
    ]

    for table in tables:

        print(f"Building Silver -> {table}")

        manager.process(
            bronze_path=f"data/bronze/{table}.parquet",
            table_name=table,
            cleaning_config=cleaning_config,
            standardization_config=standardization_config,
            deduplication_config=deduplication_config,
            schema=schema,
        )

    print("\nSilver Layer Built Successfully.")


if __name__ == "__main__":
    build_silver()