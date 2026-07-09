"""
validation_manager.py

Manages dataset validation by selecting the appropriate
expectation suite and invoking the validator.
"""

import pandas as pd

from src.utils.logger import get_logger
from src.validation.expectation_suite import EXPECTATION_SUITES
from src.validation.validator import validate_dataframe

logger = get_logger(__name__)


def validate_dataset(
    dataframe: pd.DataFrame,
    dataset_name: str,
) -> bool:
    """
    Validate a dataset using its corresponding expectation suite.

    Parameters
    ----------
    dataframe : pd.DataFrame
        DataFrame to validate.

    dataset_name : str
        Dataset name.

    Returns
    -------
    bool
        True if validation succeeds, otherwise False.
    """

    logger.info(f"Starting validation for dataset: {dataset_name}")

    expectation_suite = EXPECTATION_SUITES.get(dataset_name)

    if expectation_suite is None:
        raise ValueError(
            f"No expectation suite found for dataset '{dataset_name}'."
        )

    validation_result = validate_dataframe(
        dataframe=dataframe,
        expectation_suite=expectation_suite,
    )

    if validation_result:
        logger.info(f"{dataset_name} validation passed.")
    else:
        logger.warning(f"{dataset_name} validation failed.")

    return validation_result