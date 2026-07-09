import pandas as pd

files = [
    "products",
    "sellers",
    "geolocation",
    "orders",
    "order_items",
    "payments",
]

for file in files:
    df = pd.read_parquet(f"data/silver/{file}.parquet")
    print(f"\n{file}")
    print(df.columns.tolist())