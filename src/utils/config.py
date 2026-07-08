#Read configuration, Dataset path, Output paths, Database configuration
"""
initialize_sources.py

Initializes the enterprise source systems for the Data Engineering Pipeline.

Responsibilities:
1. Read the original Olist CSV dataset.
2. Convert selected datasets into CSV, JSON, and XML.
3. Load selected datasets into PostgreSQL.
"""

from pathlib import Path

import pandas as pd

from src.utils.logger import logger
from src.utils.config import settings
from src.utils.database import get_engine


def create_directories() -> None:
    """
    Create the required source directories if they do not exist.
    """
    directories = [
        Path("data/source/csv"),
        Path("data/source/json"),
        Path("data/source/xml"),
    ]

    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)

    logger.info("Source directories created successfully.")


def load_source_datasets():
    """
    Read all CSV datasets from the original dataset location.
    """
    dataset_path = Path(settings.DATASET_PATH)

    datasets = {
        "customers": pd.read_csv(dataset_path / "olist_customers_dataset.csv"),
        "geolocation": pd.read_csv(dataset_path / "olist_geolocation_dataset.csv"),
        "orders": pd.read_csv(dataset_path / "olist_orders_dataset.csv"),
        "order_items": pd.read_csv(dataset_path / "olist_order_items_dataset.csv"),
        "payments": pd.read_csv(dataset_path / "olist_order_payments_dataset.csv"),
        "reviews": pd.read_csv(dataset_path / "olist_order_reviews_dataset.csv"),
        "products": pd.read_csv(dataset_path / "olist_products_dataset.csv"),
        "sellers": pd.read_csv(dataset_path / "olist_sellers_dataset.csv"),
        "category_translation": pd.read_csv(
            dataset_path / "product_category_name_translation.csv"
        ),
    }

    logger.info("All source datasets loaded successfully.")

    return datasets


def main():

    logger.info("=" * 60)
    logger.info("Initializing Enterprise Source Systems")
    logger.info("=" * 60)

    create_directories()

    datasets = load_source_datasets()

    logger.info(f"Loaded {len(datasets)} datasets.")

    logger.info("Source initialization completed successfully.")


if __name__ == "__main__":
    main()