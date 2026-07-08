from src.ingestion.postgres_ingestion import read_table


def main():

    df = read_table("payments")

    print("=" * 60)
    print("POSTGRES INGESTION TEST")
    print("=" * 60)

    print(df.head())

    print("\nShape:", df.shape)
    print("\nColumns:", list(df.columns))
    print("\nDtypes:\n", df.dtypes)


if __name__ == "__main__":
    main()