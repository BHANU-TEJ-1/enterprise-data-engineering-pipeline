"""
scd_manager.py

Handles Slowly Changing Dimension (SCD) operations.
"""

import pandas as pd

from src.utils.logger import get_logger


logger = get_logger(__name__)


class SCDManager:
    """
    Applies SCD Type 1 and Type 2 operations.
    """

    def __init__(self):
        logger.info("SCD Manager Initialized.")

    # ======================================================
    # SCD TYPE 1
    # ======================================================

    def apply_type1(
        self,
        dataframe: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        SCD Type 1.

        Overwrite existing values.
        """

        logger.info("Applying SCD Type 1.")

        dataframe = dataframe.copy()

        logger.info("SCD Type 1 completed.")

        return dataframe

    # ======================================================
    # SCD TYPE 2
    # ======================================================

    def apply_type2(
        self,
        dataframe: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        SCD Type 2.

        Preserve historical records.
        """

        logger.info("Applying SCD Type 2.")

        dataframe = dataframe.copy()

        if "effective_date" not in dataframe.columns:
            dataframe["effective_date"] = (
                pd.Timestamp.today().normalize()
            )

        if "expiry_date" not in dataframe.columns:
            dataframe["expiry_date"] = pd.NaT

        if "is_current" not in dataframe.columns:
            dataframe["is_current"] = True

        logger.info("SCD Type 2 completed.")

        return dataframe