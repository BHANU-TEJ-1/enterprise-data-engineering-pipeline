"""
fact_builder.py

Builds Fact tables from the Silver Layer.
"""

import pandas as pd

from src.utils.logger import get_logger


logger = get_logger(__name__)


class FactBuilder:
    """
    Builds warehouse fact tables.
    """

    def __init__(self):
        logger.info("Fact Builder Initialized.")

    def build_sales_fact(
        self,
        orders_df: pd.DataFrame,
        order_items_df: pd.DataFrame,
        payments_df: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        Build Sales Fact Table.
        """

        raise NotImplementedError(
            "Sales Fact not implemented yet."
        )