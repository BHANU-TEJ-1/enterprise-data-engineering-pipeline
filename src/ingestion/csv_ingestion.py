"""
csv_ingestion.py

Handles CSV data ingestion for the enterprise ETL pipeline.
"""

from pathlib import Path

import pandas as pd

from src.utils.logger import get_logger

logger = get_logger(__name__)


def read_csv(source_path: str | Path) -> pd.DataFrame:
    """
    Read a CSV file and return it as a pandas DataFrame.

    Parameters
    ----------
    source_path : str | Path
        Path to the CSV file.

    Returns
    -------
    pd.DataFrame
        DataFrame containing the CSV data.

    Raises
    ------
    FileNotFoundError
        If the file does not exist.
    RuntimeError
        If the CSV cannot be read.
    """

    source_path = Path(source_path)

    logger.info(f"Reading CSV source: {source_path}")

    if not source_path.exists():
        logger.error(f"CSV file not found: {source_path}")
        raise FileNotFoundError(f"{source_path} does not exist.")

    try:
        dataframe = pd.read_csv(source_path)

        logger.info(
            f"Successfully loaded {len(dataframe)} rows "
            f"and {len(dataframe.columns)} columns."
        )

        return dataframe

    except Exception as exc:
        logger.exception("Failed to read CSV file.")
        raise RuntimeError(f"Unable to read CSV file: {source_path}") from exc