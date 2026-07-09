"""
cleaner.py

Provides reusable data cleaning utilities for the Silver Layer.

Responsibilities:
- Trim whitespace
- Replace empty strings with NaN
- Drop completely empty rows
- Fill missing values

This module intentionally contains no business-specific logic.
"""

import pandas as pd

from src.utils.logger import get_logger


logger = get_logger(__name__)


class Cleaner:
    """
    Generic DataFrame cleaner for the Silver Layer.
    """

    def __init__(self):
        logger.info("Cleaner initialized.")

    def trim_whitespace(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Remove leading and trailing whitespace
        from all string columns.
        """
        try:
            logger.info("Trimming whitespace...")

            df = df.copy()

            object_columns = df.select_dtypes(include=["object"]).columns

            for column in object_columns:
                df[column] = df[column].str.strip()

            logger.info("Whitespace trimming completed.")

            return df

        except Exception:
            logger.exception("Failed while trimming whitespace.")
            raise

    def replace_empty_strings(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Replace empty strings and whitespace-only strings with NaN.
        """
        try:
            logger.info("Replacing empty strings with NaN...")

            df = df.copy()

            df.replace(r'^\s*$', pd.NA, regex=True, inplace=True)

            logger.info("Empty string replacement completed.")

            return df

        except Exception:
            logger.exception("Failed while replacing empty strings.")
            raise

    def drop_empty_rows(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Remove rows where every column is missing.
        """
        try:
            logger.info("Dropping completely empty rows...")

            df = df.copy()

            df.dropna(how="all", inplace=True)

            logger.info("Empty rows removed successfully.")

            return df

        except Exception:
            logger.exception("Failed while dropping empty rows.")
            raise

    def fill_missing_values(
        self,
        df: pd.DataFrame,
        value
    ) -> pd.DataFrame:
        """
        Fill missing values with the provided value.
        """
        try:
            logger.info(f"Filling missing values with '{value}'...")

            df = df.copy()

            df.fillna(value, inplace=True)

            logger.info("Missing values filled successfully.")

            return df

        except Exception:
            logger.exception("Failed while filling missing values.")
            raise

    def clean(
        self,
        df: pd.DataFrame,
        trim_whitespace: bool = True,
        replace_empty: bool = True,
        drop_empty_rows: bool = True,
        fill_missing: bool = False,
        fill_value=None,
    ) -> pd.DataFrame:
        """
        Execute selected cleaning operations
        in a predefined sequence.
        """
        try:
            logger.info("Starting cleaning pipeline...")

            if trim_whitespace:
                df = self.trim_whitespace(df)

            if replace_empty:
                df = self.replace_empty_strings(df)

            if drop_empty_rows:
                df = self.drop_empty_rows(df)

            if fill_missing:
                df = self.fill_missing_values(df, fill_value)

            logger.info("Cleaning pipeline completed successfully.")

            return df

        except Exception:
            logger.exception("Cleaning pipeline failed.")
            raise