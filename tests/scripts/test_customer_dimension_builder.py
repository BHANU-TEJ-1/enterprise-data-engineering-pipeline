import pandas as pd

from src.utils.logger import get_logger


class CustomerDimensionBuilder:
    """
    Builds the Customer Dimension from the Silver layer.
    """

    def __init__(self):
        self.logger = get_logger(__name__)

    def build(self, customers_df: pd.DataFrame) -> pd.DataFrame:
      """
      Build the customer dimension.
      """

      self.logger.info("Building Customer Dimension.")

      dimension_df = customers_df[
          [
              "customer_id",
              "customer_name",
          ]
      ].drop_duplicates()

      self.logger.info(
          f"Customer Dimension created with {len(dimension_df)} rows."
      )

      return dimension_df