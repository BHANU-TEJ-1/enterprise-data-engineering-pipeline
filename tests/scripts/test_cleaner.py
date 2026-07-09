import pandas as pd

from src.silver.cleaner import Cleaner


def main():

    cleaner = Cleaner()

    # Sample DataFrame
    df = pd.DataFrame(
        {
            "name": [" John ", "Alice", "   ", None],
            "age": [25, None, None, None],
            "city": [" New York ", "", None, None],
        }
    )

    print("\nOriginal DataFrame")
    print(df)

    # --------------------------------------------------
    # Test trim_whitespace
    # --------------------------------------------------

    trimmed_df = cleaner.trim_whitespace(df)

    print("\nAfter trim_whitespace()")
    print(trimmed_df)

    # --------------------------------------------------
    # Test replace_empty_strings
    # --------------------------------------------------

    replaced_df = cleaner.replace_empty_strings(trimmed_df)

    print("\nAfter replace_empty_strings()")
    print(replaced_df)

    # --------------------------------------------------
    # Test drop_empty_rows
    # --------------------------------------------------

    dropped_df = cleaner.drop_empty_rows(replaced_df)

    print("\nAfter drop_empty_rows()")
    print(dropped_df)

    # --------------------------------------------------
    # Test fill_missing_values
    # --------------------------------------------------

    filled_df = cleaner.fill_missing_values(
        dropped_df,
        value="Unknown"
    )

    print("\nAfter fill_missing_values()")
    print(filled_df)

    # --------------------------------------------------
    # Test complete cleaning pipeline
    # --------------------------------------------------

    cleaned_df = cleaner.clean(
        df,
        fill_missing=True,
        fill_value="Unknown",
    )

    print("\nAfter clean()")
    print(cleaned_df)


if __name__ == "__main__":
    main()