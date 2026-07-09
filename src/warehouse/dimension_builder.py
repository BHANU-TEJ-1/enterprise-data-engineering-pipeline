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

    def build_customer_dimension(
        self,
        customers_df: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        Build Customer Dimension.
        """

        logger.info("Building Customer Dimension.")

        dimension_df = (
            customers_df
            .drop_duplicates()
            .reset_index(drop=True)
        )

        logger.info(
            f"Customer Dimension created with {len(dimension_df)} rows."
        )

        return dimension_df

    def build_product_dimension(
        self,
        products_df: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        Build Product Dimension.
        """

        raise NotImplementedError(
            "Product Dimension not implemented yet."
        )

    def build_seller_dimension(
        self,
        sellers_df: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        Build Seller Dimension.
        """

        raise NotImplementedError(
            "Seller Dimension not implemented yet."
        )

    def build_geolocation_dimension(
        self,
        geolocation_df: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        Build Geolocation Dimension.
        """

        raise NotImplementedError(
            "Geolocation Dimension not implemented yet."
        )

    def build_date_dimension(
        self,
        dataframe: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        Build Date Dimension.
        """

        raise NotImplementedError(
            "Date Dimension not implemented yet."
        )