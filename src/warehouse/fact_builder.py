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

        logger.info("Building Sales Fact.")

        fact_df = orders_df.merge(
            order_items_df,
            on="order_id",
            how="inner",
        )

        fact_df = fact_df.merge(
            payments_df,
            on="order_id",
            how="left",
        )

        fact_df.insert(
            0,
            "sales_sk",
            range(1, len(fact_df) + 1),
        )

        columns = [
            "sales_sk",
            "order_id",
            "customer_id",
            "product_id",
            "seller_id",
            "payment_type",
            "payment_value",
            "price",
            "freight_value",
            "order_purchase_timestamp",
            "order_status",
        ]

        fact_df = fact_df[columns]

        logger.info(
            f"Sales Fact created with {len(fact_df)} rows."
        )

        return fact_df