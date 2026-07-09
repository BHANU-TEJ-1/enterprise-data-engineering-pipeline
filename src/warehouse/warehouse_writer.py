from pathlib import Path

import pandas as pd

from src.utils.logger import get_logger


class WarehouseWriter:
    """
    Writes DataFrames to the Data Warehouse layer.
    """

    def __init__(self, warehouse_path: str):
        self.logger = get_logger(__name__)
        self.warehouse_path = Path(warehouse_path)
        self.warehouse_path.mkdir(parents=True, exist_ok=True)

    def write_parquet(self, dataframe: pd.DataFrame, table_name: str) -> Path:
        """
        Write a DataFrame as a Parquet file.
        """
        output_path = self.warehouse_path / f"{table_name}.parquet"

        try:
            dataframe.to_parquet(
                output_path,
                index=False,
                compression="snappy",
            )

            self.logger.info(f"Warehouse table written: {output_path}")
            return output_path

        except Exception as e:
            self.logger.exception(f"Failed to write warehouse table: {table_name}")
            raise