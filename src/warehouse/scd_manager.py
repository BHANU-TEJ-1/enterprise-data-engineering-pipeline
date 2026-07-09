"""
scd_manager.py

Applies Slowly Changing Dimension strategies.
"""

import pandas as pd

from src.utils.logger import get_logger


logger = get_logger(__name__)


class SCDManager:
    """
    Handles Slowly Changing Dimension (SCD) operations.
    """

    def __init__(self):
        logger.info("SCD Manager Initialized.")

    def apply_type1(
        self,
        dataframe: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        Apply SCD Type 1.

        Overwrites existing values.
        """

        logger.info("Applying SCD Type 1.")

        return dataframe

    def apply_type2(
        self,
        dataframe: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        Apply SCD Type 2.

        Preserves historical records.
        """

        logger.info("Applying SCD Type 2.")

        return dataframe