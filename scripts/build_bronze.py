"""
build_bronze.py

Build the complete Bronze Layer.
"""

from src.bronze.bronze_layer import BronzeLayer
from src.ingestion.ingestion_manager import ingest


def build_bronze():

    bronze = BronzeLayer()

    sources = [

        # ------------------------------------
        # CSV
        # ------------------------------------

        (
            "csv",
            "data/source/csv/customers.csv",
            "customers",
        ),

        (
            "csv",
            "data/source/csv/geolocation.csv",
            "geolocation",
        ),

        # ------------------------------------
        # JSON
        # ------------------------------------

        (
            "json",
            "data/source/json/orders.json",
            "orders",
        ),

        (
            "json",
            "data/source/json/order_items.json",
            "order_items",
        ),

        # ------------------------------------
        # XML
        # ------------------------------------

        (
            "xml",
            "data/source/xml/products.xml",
            "products",
        ),

        (
            "xml",
            "data/source/xml/product_category_translation.xml",
            "category_translation",
        ),

        # ------------------------------------
        # PostgreSQL
        # ------------------------------------

        (
            "postgres",
            "payments",
            "payments",
        ),

        (
            "postgres",
            "sellers",
            "sellers",
        ),

        (
            "postgres",
            "reviews",
            "reviews",
        ),
    ]

    for source_type, source, table_name in sources:

        print(f"Building Bronze -> {table_name}")

        df = ingest(
            source_type,
            source,
        )

        bronze.write_parquet(
            df=df,
            table_name=table_name,
        )

    print("\nBronze Layer Built Successfully.")


if __name__ == "__main__":
    build_bronze()