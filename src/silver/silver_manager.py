"""
silver_manager.py

Orchestrates the complete Silver Layer pipeline.

Pipeline:
Bronze Parquet
      ↓
Cleaner
      ↓
Standardizer
      ↓
Deduplicator
      ↓
DatatypeConverter
      ↓
Silver Layer
"""

import pandas as pd

from src.silver.cleaner import Cleaner
from src.silver.standardizer import Standardizer
from src.silver.deduplicator import Deduplicator
from src.silver.datatype_converter import DatatypeConverter
from src.silver.silver_layer import SilverLayer

from src.utils.logger import get_logger


logger = get_logger(__name__)


class SilverManager:
    """
    Orchestrates the complete Silver Layer pipeline.
    """

    def __init__(self):

        self.cleaner = Cleaner()
        self.standardizer = Standardizer()
        self.deduplicator = Deduplicator()
        self.converter = DatatypeConverter()
        self.silver_layer = SilverLayer()

        logger.info("SilverManager initialized.")

    def process(
        self,
        bronze_path: str,
        table_name: str,
        cleaning_config: dict,
        standardization_config: dict,
        deduplication_config: dict,
        schema: dict,
    ) -> str:
        """
        Execute the complete Silver pipeline.

        Returns
        -------
        str
            Output parquet path.
        """

        try:

            logger.info(
                f"Starting Silver pipeline for '{table_name}'."
            )

            # ----------------------------------------
            # Read Bronze Parquet
            # ----------------------------------------

            df = pd.read_parquet(bronze_path)

            logger.info(
                f"Loaded Bronze data: {len(df)} rows."
            )

            # ----------------------------------------
            # Cleaning
            # ----------------------------------------

            df = self.cleaner.clean(
                df,
                **cleaning_config
            )

            # ----------------------------------------
            # Standardization
            # ----------------------------------------

            df = self.standardizer.standardize(
                df,
                **standardization_config
            )

            # ----------------------------------------
            # Deduplication
            # ----------------------------------------

            df = self.deduplicator.deduplicate(
                df,
                **deduplication_config
            )

            # ----------------------------------------
            # Datatype Conversion
            # ----------------------------------------

            df = self.converter.convert(
                df,
                schema
            )

            # ----------------------------------------
            # Write Silver Layer
            # ----------------------------------------

            output_path = self.silver_layer.write_parquet(
                df=df,
                table_name=table_name,
            )

            logger.info(
                f"Silver pipeline completed for '{table_name}'."
            )

            return output_path

        except Exception:

            logger.exception(
                f"Silver pipeline failed for '{table_name}'."
            )

            raise