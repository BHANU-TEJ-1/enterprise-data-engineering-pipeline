"""
bronze_layer.py

Writes raw ingested data into the Bronze Layer as Parquet files.
"""

from pathlib import Path

import pandas as pd

from src.utils.logger import get_logger

logger = get_logger(__name__)


def write_to_bronze(dataframe: pd.DataFrame, dataset_name: str) -> None:
    """
    Write a DataFrame to the Bronze Layer.

    Parameters
    ----------
    dataframe : pd.DataFrame
        DataFrame to be stored.

    dataset_name : str
        Name of the dataset.

    Raises
    ------
    RuntimeError
        If writing the parquet file fails.
    """

    bronze_directory = Path("data/bronze")
    bronze_directory.mkdir(parents=True, exist_ok=True)

    output_path = bronze_directory / f"{dataset_name}.parquet"

    logger.info(f"Writing Bronze dataset: {output_path}")

    try:

        dataframe.to_parquet(
            output_path,
            index=False,
            compression="snappy",
        )

        logger.info(
            f"Bronze dataset '{dataset_name}' written successfully."
        )

    except Exception as exc:

        logger.exception("Failed to write Bronze dataset.")

        raise RuntimeError(
            f"Unable to write Bronze dataset: {dataset_name}"
        ) from exc