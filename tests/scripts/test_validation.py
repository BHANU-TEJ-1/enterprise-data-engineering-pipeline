from pathlib import Path

import pandas as pd

from src.validation.validation_manager import validate_dataset


def main():

    df = pd.read_parquet(
        Path("data/bronze/customers.parquet")
    )

    result = validate_dataset(
        dataframe=df,
        dataset_name="customers",
    )

    print("\nValidation Result :", result)


if __name__ == "__main__":
    main()