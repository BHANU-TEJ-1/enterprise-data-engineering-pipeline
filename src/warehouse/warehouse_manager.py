"""
warehouse_manager.py

Orchestrates Data Warehouse creation.
"""

import pandas as pd

from src.utils.logger import get_logger

from src.warehouse.dimension_builder import DimensionBuilder
from src.warehouse.fact_builder import FactBuilder
from src.warehouse.scd_manager import SCDManager
from src.warehouse.warehouse_writer import WarehouseWriter


logger = get_logger(__name__)


class WarehouseManager:
    """
    Orchestrates warehouse creation.
    """

    def __init__(
        self,
        output_directory: str = "data/gold",
    ):

        self.dimension_builder = DimensionBuilder()
        self.fact_builder = FactBuilder()
        self.scd_manager = SCDManager()
        self.writer = WarehouseWriter(output_directory)

        logger.info("Warehouse Manager Initialized.")

    # ======================================================
    # Customer Dimension
    # ======================================================

    def build_customer_dimension(
        self,
        customers_df: pd.DataFrame,
    ) -> str:

        logger.info("Building Customer Dimension.")

        df = self.dimension_builder.build_customer_dimension(
            customers_df
        )

        df = self.scd_manager.apply_type2(df)

        return self.writer.write_parquet(
            dataframe=df,
            table_name="dim_customer",
        )

    # ======================================================
    # Product Dimension
    # ======================================================

    def build_product_dimension(
        self,
        products_df: pd.DataFrame,
    ) -> str:

        logger.info("Building Product Dimension.")

        df = self.dimension_builder.build_product_dimension(
            products_df
        )

        return self.writer.write_parquet(
            dataframe=df,
            table_name="dim_product",
        )

    # ======================================================
    # Seller Dimension
    # ======================================================

    def build_seller_dimension(
        self,
        sellers_df: pd.DataFrame,
    ) -> str:

        logger.info("Building Seller Dimension.")

        df = self.dimension_builder.build_seller_dimension(
            sellers_df
        )

        return self.writer.write_parquet(
            dataframe=df,
            table_name="dim_seller",
        )

    # ======================================================
    # Geolocation Dimension
    # ======================================================

    def build_geolocation_dimension(
        self,
        geolocation_df: pd.DataFrame,
    ) -> str:

        logger.info("Building Geolocation Dimension.")

        df = self.dimension_builder.build_geolocation_dimension(
            geolocation_df
        )

        return self.writer.write_parquet(
            dataframe=df,
            table_name="dim_geolocation",
        )

    # ======================================================
    # Sales Fact
    # ======================================================

    def build_sales_fact(
        self,
        orders_df: pd.DataFrame,
        order_items_df: pd.DataFrame,
        payments_df: pd.DataFrame,
    ) -> str:

        logger.info("Building Sales Fact.")

        df = self.fact_builder.build_sales_fact(
            orders_df,
            order_items_df,
            payments_df,
        )

        return self.writer.write_parquet(
            dataframe=df,
            table_name="fact_sales",
        )