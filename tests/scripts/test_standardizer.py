import pandas as pd

from src.silver.standardizer import Standardizer


def main():

    standardizer = Standardizer()

    # Sample DataFrame
    df = pd.DataFrame(
        {
            " Customer Name ": ["john doe", "ALICE smith"],
            "City": ["new york", "LONDON"],
            "Email": ["john@gmail.com", "ALICE@MAIL.COM"],
            "Order-Date": ["2024/01/05", "01-02-2024"],
        }
    )

    print("\nOriginal DataFrame")
    print(df)

    # --------------------------------------------------
    # Test column name standardization
    # --------------------------------------------------

    column_df = standardizer.standardize_column_names(df)

    print("\nAfter standardize_column_names()")
    print(column_df)

    # --------------------------------------------------
    # Test text standardization
    # --------------------------------------------------

    text_df = standardizer.standardize_text_case(
        column_df,
        columns=[
            "customer_name",
            "city",
            "country",  # Intentionally missing
        ],
    )

    print("\nAfter standardize_text_case()")
    print(text_df)

    # --------------------------------------------------
    # Test date standardization
    # --------------------------------------------------

    date_df = standardizer.standardize_dates(
        text_df,
        columns=[
            "order_date",
        ],
    )

    print("\nAfter standardize_dates()")
    print(date_df)

    # --------------------------------------------------
    # Test full pipeline
    # --------------------------------------------------

    standardized_df = standardizer.standardize(
        df,
        text_columns=[
            "customer_name",
            "city",
        ],
        date_columns=[
            "order_date",
        ],
    )

    print("\nAfter standardize()")
    print(standardized_df)


if __name__ == "__main__":
    main()