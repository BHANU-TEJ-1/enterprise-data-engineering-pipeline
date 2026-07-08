"""
postgres_ingestion.py

Handles PostgreSQL data ingestion for the enterprise ETL pipeline.
"""

import pandas as pd

from src.utils.database import get_engine
from src.utils.logger import get_logger

logger = get_logger(__name__)


def read_table(table_name: str) -> pd.DataFrame:
    """
    Read a PostgreSQL table and return it as a pandas DataFrame.
    """

    logger.info(f"Reading PostgreSQL table: {table_name}")

    try:
        engine = get_engine()

        query = f"SELECT * FROM {table_name};"

        dataframe = pd.read_sql(query, engine)

        logger.info(
            f"Successfully loaded {len(dataframe)} rows "
            f"and {len(dataframe.columns)} columns."
        )

        return dataframe

    except Exception as exc:
        logger.exception("Failed to read PostgreSQL table.")
        raise RuntimeError(f"Unable to read table: {table_name}") from exc