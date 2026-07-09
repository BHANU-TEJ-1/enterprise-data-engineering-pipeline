"""
dimension_builder.py

Builds Dimension tables from the Silver Layer.
"""

import pandas as pd

from src.utils.logger import get_logger


logger = get_logger(__name__)


class DimensionBuilder:
    """
    Builds warehouse dimension tables.
    """

    def __init__(self):
        logger.info("Dimension Builder Initialized.")

    # -------------------------------------------------------
    # Customer Dimension
    # -------------------------------------------------------

    def build_customer_dimension(
        self,
        customers_df: pd.DataFrame,
    ) -> pd.DataFrame:

        logger.info("Building Customer Dimension.")

        df = (
            customers_df
            .drop_duplicates()
            .reset_index(drop=True)
            .copy()
        )

        df.insert(
            0,
            "customer_sk",
            range(1, len(df) + 1),
        )

        df["effective_date"] = pd.Timestamp.today().normalize()
        df["expiry_date"] = pd.NaT
        df["is_current"] = True

        return df

    # -------------------------------------------------------
    # Product Dimension
    # -------------------------------------------------------

    def build_product_dimension(
        self,
        products_df: pd.DataFrame,
    ) -> pd.DataFrame:

        logger.info("Building Product Dimension.")

        df = (
            products_df
            .drop_duplicates()
            .reset_index(drop=True)
            .copy()
        )

        df.insert(
            0,
            "product_sk",
            range(1, len(df) + 1),
        )

        return df

    # -------------------------------------------------------
    # Seller Dimension
    # -------------------------------------------------------

    def build_seller_dimension(
        self,
        sellers_df: pd.DataFrame,
    ) -> pd.DataFrame:

        logger.info("Building Seller Dimension.")

        df = (
            sellers_df
            .drop_duplicates()
            .reset_index(drop=True)
            .copy()
        )

        df.insert(
            0,
            "seller_sk",
            range(1, len(df) + 1),
        )

        return df

    # -------------------------------------------------------
    # Geolocation Dimension
    # -------------------------------------------------------

    def build_geolocation_dimension(
        self,
        geolocation_df: pd.DataFrame,
    ) -> pd.DataFrame:

        logger.info("Building Geolocation Dimension.")

        df = (
            geolocation_df
            .drop_duplicates()
            .reset_index(drop=True)
            .copy()
        )

        df.insert(
            0,
            "geo_sk",
            range(1, len(df) + 1),
        )

        return df