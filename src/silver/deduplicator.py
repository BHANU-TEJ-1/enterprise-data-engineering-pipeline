"""
deduplicator.py

Provides reusable duplicate removal utilities
for the Silver Layer.

Responsibilities:
- Remove duplicate rows

This module intentionally contains no business-specific logic.
"""

import pandas as pd

from src.utils.logger import get_logger


logger = get_logger(__name__)


class Deduplicator:
    """
    Generic DataFrame deduplicator for the Silver Layer.
    """

    def __init__(self):
        logger.info("Deduplicator initialized.")

    def remove_duplicates(
        self,
        df: pd.DataFrame,
        subset: list[str] | None = None,
        keep: str | bool = "first",
    ) -> pd.DataFrame:
        """
        Remove duplicate rows from a DataFrame.

        Parameters
        ----------
        df : pd.DataFrame
            Input DataFrame.

        subset : list[str] | None
            Columns to consider when identifying duplicates.
            If None, the entire row is considered.

        keep : {"first", "last", False}
            Which duplicate to keep.
        """
        try:
            logger.info("Removing duplicate rows...")

            df = df.copy()

            before_count = len(df)

            df = df.drop_duplicates(
                subset=subset,
                keep=keep,
            )

            after_count = len(df)

            removed_count = before_count - after_count

            logger.info(
                f"Duplicate removal completed. "
                f"Removed {removed_count} duplicate rows."
            )

            return df

        except Exception:
            logger.exception("Failed while removing duplicate rows.")
            raise

    def deduplicate(
        self,
        df: pd.DataFrame,
        subset: list[str] | None = None,
        keep: str | bool = "first",
    ) -> pd.DataFrame:
        """
        Execute duplicate removal.
        """
        try:
            logger.info("Starting deduplication pipeline...")

            df = self.remove_duplicates(
                df=df,
                subset=subset,
                keep=keep,
            )

            logger.info("Deduplication pipeline completed successfully.")

            return df

        except Exception:
            logger.exception("Deduplication pipeline failed.")
            raise