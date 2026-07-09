import pandas as pd

from src.utils.logger import get_logger
from src.warehouse.dimensions.customer_dimension_builder import (
    CustomerDimensionBuilder,
)
from src.warehouse.warehouse_writer import WarehouseWriter


class WarehouseManager:
    """
    Orchestrates the Data Warehouse creation process.
    """

    def __init__(self, warehouse_path: str):
        self.logger = get_logger(__name__)

        self.writer = WarehouseWriter(warehouse_path)
        self.customer_builder = CustomerDimensionBuilder()

    def build_customer_dimension(self, customers_df: pd.DataFrame):
        """
        Build and write the Customer Dimension.
        """

        self.logger.info("Starting Customer Dimension creation.")

        dimension_df = self.customer_builder.build(customers_df)

        self.writer.write_parquet(
            dataframe=dimension_df,
            table_name="dim_customer",
        )

        self.logger.info("Customer Dimension created successfully.")