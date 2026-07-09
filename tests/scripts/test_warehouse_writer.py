import pandas as pd

from src.warehouse.warehouse_writer import WarehouseWriter


def main():
    df = pd.DataFrame(
        {
            "id": [1, 2, 3],
            "name": ["Alice", "Bob", "Charlie"],
        }
    )

    writer = WarehouseWriter("data/gold")

    path = writer.write_parquet(
        dataframe=df,
        table_name="dim_customer",
    )

    print(f"\nWarehouse table created successfully!")
    print(path)


if __name__ == "__main__":
    main()