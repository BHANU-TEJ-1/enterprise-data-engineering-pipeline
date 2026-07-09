"""
silver_layer.py

Writes processed DataFrames
to the Silver Layer.
"""

from pathlib import Path

import pandas as pd

from src.utils.logger import get_logger


logger = get_logger(__name__)


class SilverLayer:
    """
    Writes DataFrames to the Silver layer.
    """

    def __init__(self, output_directory: str = "data/silver"):

        self.output_directory = Path(output_directory)

        self.output_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

        logger.info(
            f"Silver output directory: {self.output_directory}"
        )

    def write(
        self,
        df: pd.DataFrame,
        table_name: str,
    ) -> str:
        """
        Write DataFrame to a parquet file.

        Returns
        -------
        str
            Path of the written parquet file.
        """

        try:

            output_path = (
                self.output_directory /
                f"{table_name}.parquet"
            )

            logger.info(
                f"Writing '{table_name}' to Silver Layer..."
            )

            df.to_parquet(
                output_path,
                index=False,
                compression="snappy",
            )

            logger.info(
                f"Successfully wrote {output_path}"
            )

            return str(output_path)

        except Exception:

            logger.exception(
                f"Failed writing '{table_name}'"
            )

            raise