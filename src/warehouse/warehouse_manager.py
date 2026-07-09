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

    def build_customer_dimension(
        self,
        customers_df: pd.DataFrame,
    ) -> None:
        """
        Build Customer Dimension.
        """

        logger.info("Building Customer Dimension.")

        dimension_df = (
            self.dimension_builder
            .build_customer_dimension(customers_df)
        )

        dimension_df = (
            self.scd_manager
            .apply_type1(dimension_df)
        )

        self.writer.write_parquet(
            dataframe=dimension_df,
            table_name="dim_customer",
        )

        logger.info("Customer Dimension Created Successfully.")

    def build_sales_fact(self):
        """
        Build Sales Fact Table.
        """

        raise NotImplementedError(
            "Sales Fact not implemented yet."
        )