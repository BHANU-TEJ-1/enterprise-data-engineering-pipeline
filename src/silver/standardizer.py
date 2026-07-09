"""
standardizer.py

Provides reusable data standardization utilities
for the Silver Layer.

Responsibilities:
- Standardize column names
- Standardize text columns
- Standardize date columns

This module intentionally contains no business-specific logic.
"""

import pandas as pd

from src.utils.logger import get_logger


logger = get_logger(__name__)


class Standardizer:
    """
    Generic DataFrame standardizer for the Silver Layer.
    """

    def __init__(self):
        logger.info("Standardizer initialized.")

    def standardize_column_names(
        self,
        df: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        Standardize DataFrame column names.

        Rules:
        - Trim whitespace
        - Convert to lowercase
        - Replace spaces with underscores
        - Replace hyphens with underscores
        """
        try:
            logger.info("Standardizing column names...")

            df = df.copy()

            df.columns = (
                df.columns
                .str.strip()
                .str.lower()
                .str.replace(" ", "_")
                .str.replace("-", "_")
            )

            logger.info("Column names standardized successfully.")

            return df

        except Exception:
            logger.exception("Failed to standardize column names.")
            raise

    def standardize_text_case(
        self,
        df: pd.DataFrame,
        columns: list[str],
    ) -> pd.DataFrame:
        """
        Convert selected text columns to Title Case.
        """
        try:
            logger.info("Standardizing text columns...")

            df = df.copy()

            for column in columns:

                if column not in df.columns:
                    logger.warning(f"Column '{column}' not found. Skipping.")
                    continue

                df[column] = df[column].astype("string").str.title()

            logger.info("Text standardization completed.")

            return df

        except Exception:
            logger.exception("Failed while standardizing text columns.")
            raise

    def standardize_dates(
        self,
        df: pd.DataFrame,
        columns: list[str],
        date_format: str = "%Y-%m-%d",
    ) -> pd.DataFrame:
        """
        Standardize selected date columns.
        """
        try:
            logger.info("Standardizing date columns...")

            df = df.copy()

            for column in columns:

                if column not in df.columns:
                    logger.warning(f"Column '{column}' not found. Skipping.")
                    continue

                df[column] = pd.to_datetime(
                    df[column],
                    errors="coerce",
                ).dt.strftime(date_format)

            logger.info("Date standardization completed.")

            return df

        except Exception:
            logger.exception("Failed while standardizing date columns.")
            raise

    def standardize(
        self,
        df: pd.DataFrame,
        text_columns: list[str] | None = None,
        date_columns: list[str] | None = None,
    ) -> pd.DataFrame:
        """
        Execute the standardization pipeline.
        """
        try:
            logger.info("Starting standardization pipeline...")

            df = self.standardize_column_names(df)

            if text_columns:
                df = self.standardize_text_case(
                    df,
                    text_columns,
                )

            if date_columns:
                df = self.standardize_dates(
                    df,
                    date_columns,
                )

            logger.info("Standardization pipeline completed successfully.")

            return df

        except Exception:
            logger.exception("Standardization pipeline failed.")
            raise