"""
build_bronze.py

Build the complete Bronze Layer.
"""

from src.bronze.bronze_layer import BronzeLayer
from src.ingestion.ingestion_manager import ingest


def main():

    bronze = BronzeLayer()

    sources = [

        # CSV
        ("csv", r"C:\Users\TEJ\OneDrive\Desktop\EnterpriseDataSources\CRM\customers.csv", "customers"),
        ("csv", r"C:\Users\TEJ\OneDrive\Desktop\EnterpriseDataSources\CRM\geolocation.csv", "geolocation"),

        # JSON
        ("json", r"C:\Users\TEJ\OneDrive\Desktop\EnterpriseDataSources\OMS\orders.json", "orders"),
        ("json", r"C:\Users\TEJ\OneDrive\Desktop\EnterpriseDataSources\OMS\order_items.json", "order_items"),

        # XML
        ("xml", r"C:\Users\TEJ\OneDrive\Desktop\EnterpriseDataSources\PIM\products.xml", "products"),
        ("xml", r"C:\Users\TEJ\OneDrive\Desktop\EnterpriseDataSources\PIM\product_category_translation.xml", "category_translation"),

        # PostgreSQL
        ("postgres", "payments", "payments"),
        ("postgres", "sellers", "sellers"),
        ("postgres", "reviews", "reviews"),
    ]

    for source_type, source, table_name in sources:

        print(f"Building Bronze -> {table_name}")

        df = ingest(source_type, source)

        bronze.write_parquet(
            df=df,
            table_name=table_name,
        )

    print("\nBronze Layer Built Successfully.")


if __name__ == "__main__":
    main()