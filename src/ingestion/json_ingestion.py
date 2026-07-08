"""
json_ingestion.py

Handles JSON data ingestion for the enterprise ETL pipeline.
"""

from pathlib import Path

import pandas as pd

from src.utils.logger import get_logger

logger = get_logger(__name__)


def read_json(source_path: str | Path) -> pd.DataFrame:
    """
    Read a JSON file and return it as a pandas DataFrame.
    """

    source_path = Path(source_path)

    logger.info(f"Reading JSON source: {source_path}")

    if not source_path.exists():
        logger.error(f"JSON file not found: {source_path}")
        raise FileNotFoundError(f"{source_path} does not exist.")

    try:
        dataframe = pd.read_json(source_path)

        logger.info(
            f"Successfully loaded {len(dataframe)} rows "
            f"and {len(dataframe.columns)} columns."
        )

        return dataframe

    except Exception as exc:
        logger.exception("Failed to read JSON file.")
        raise RuntimeError(f"Unable to read JSON file: {source_path}") from exc