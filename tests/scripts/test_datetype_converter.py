import pandas as pd

from src.silver.datatype_converter import DatatypeConverter


def main():

    converter = DatatypeConverter()

    df = pd.DataFrame(
        {
            "customer_id": ["101", "102", "103"],
            "price": ["1200.50", "950.25", "1500"],
            "is_active": [True, False, True],
            "order_date": [
                "2024/01/01",
                "2024-02-15",
                "2024-03-20",
            ],
            "customer_name": [
                "John",
                "Alice",
                "Bob",
            ],
        }
    )

    print("\nOriginal DataFrame")
    print(df)

    print("\nOriginal dtypes")
    print(df.dtypes)

    # ----------------------------------------
    # Test single column conversion
    # ----------------------------------------

    single_df = converter.convert_column(
        df,
        column="price",
        dtype="float",
    )

    print("\nAfter converting price")
    print(single_df.dtypes)

    # ----------------------------------------
    # Test full schema conversion
    # ----------------------------------------

    schema = {
        "customer_id": "int",
        "price": "float",
        "is_active": "bool",
        "order_date": "datetime",
        "customer_name": "string",
        "missing_column": "int",   # Should log warning
    }

    converted_df = converter.convert(
        df,
        schema,
    )

    print("\nConverted DataFrame")
    print(converted_df)

    print("\nConverted dtypes")
    print(converted_df.dtypes)


if __name__ == "__main__":
    main()