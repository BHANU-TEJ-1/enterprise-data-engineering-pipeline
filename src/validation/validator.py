"""
validator.py

Generic validation engine for all datasets.
"""

import pandas as pd

from src.utils.logger import get_logger

logger = get_logger(__name__)


def validate_dataframe(
    dataframe: pd.DataFrame,
    expectation_suite: dict,
) -> bool:

    logger.info("Starting validation...")

    validation_success = True

    # -------------------------
    # Not Null Validation
    # -------------------------

    for column in expectation_suite.get("not_null", []):

        if dataframe[column].isnull().any():
            logger.warning(f"{column} contains NULL values.")
            validation_success = False

    # -------------------------
    # Unique Validation
    # -------------------------

    for column in expectation_suite.get("unique", []):

        if dataframe[column].duplicated().any():
            logger.warning(f"{column} contains duplicate values.")
            validation_success = False

    # -------------------------
    # Greater Than Zero
    # -------------------------

    for column in expectation_suite.get("greater_than_zero", []):

        if (dataframe[column] <= 0).any():
            logger.warning(f"{column} contains values <= 0.")
            validation_success = False

    if validation_success:
        logger.info("Validation Passed.")
    else:
        logger.warning("Validation Failed.")

    return validation_success