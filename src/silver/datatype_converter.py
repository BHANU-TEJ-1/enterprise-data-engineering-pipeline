"""
datatype_converter.py

Provides reusable datatype conversion utilities
for the Silver Layer.

Responsibilities:
- Convert DataFrame columns to specified datatypes.

This module intentionally contains no business-specific logic.
"""

import pandas as pd

from src.utils.logger import get_logger


logger = get_logger(__name__)


class DatatypeConverter:
    """
    Generic DataFrame datatype converter
    for the Silver Layer.
    """

    def __init__(self):
        logger.info("DatatypeConverter initialized.")

    def convert_column(
        self,
        df: pd.DataFrame,
        column: str,
        dtype: str,
    ) -> pd.DataFrame:
        """
        Convert a single DataFrame column
        to the specified datatype.
        """

        try:
            df = df.copy()

            if column not in df.columns:
                logger.warning(f"Column '{column}' not found. Skipping.")
                return df

            logger.info(f"Converting '{column}' to {dtype}...")

            dtype = dtype.lower()

            if dtype == "string":
                df[column] = df[column].astype("string")

            elif dtype == "int":
                df[column] = pd.to_numeric(
                    df[column],
                    errors="coerce",
                ).astype("Int64")

            elif dtype == "float":
                df[column] = pd.to_numeric(
                    df[column],
                    errors="coerce",
                )

            elif dtype == "bool":
                df[column] = df[column].astype("boolean")

            elif dtype == "datetime":
                df[column] = pd.to_datetime(
                    df[column],
                    errors="coerce",
                )

            else:
                raise ValueError(
                    f"Unsupported datatype: {dtype}"
                )

            logger.info(f"'{column}' converted successfully.")

            return df

        except Exception:
            logger.exception(
                f"Failed while converting '{column}'."
            )
            raise

    def convert(
        self,
        df: pd.DataFrame,
        schema: dict[str, str],
    ) -> pd.DataFrame:
        """
        Convert multiple columns using
        a schema mapping.

        Example
        -------
        schema = {
            "customer_id": "int",
            "price": "float",
            "order_date": "datetime"
        }
        """

        try:
            logger.info("Starting datatype conversion pipeline...")

            for column, dtype in schema.items():

                df = self.convert_column(
                    df=df,
                    column=column,
                    dtype=dtype,
                )

            logger.info(
                "Datatype conversion pipeline completed successfully."
            )

            return df

        except Exception:
            logger.exception(
                "Datatype conversion pipeline failed."
            )
            raise