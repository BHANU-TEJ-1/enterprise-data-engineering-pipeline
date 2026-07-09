import pandas as pd

from src.silver.silver_layer import SilverLayer


def main():

    silver = SilverLayer()

    df = pd.DataFrame(
        {
            "customer_id": [101, 102, 103],
            "customer_name": [
                "John",
                "Alice",
                "Bob",
            ],
        }
    )

    path = silver.write(
        df,
        table_name="customers",
    )

    print("\nWritten File")
    print(path)


if __name__ == "__main__":
    main()