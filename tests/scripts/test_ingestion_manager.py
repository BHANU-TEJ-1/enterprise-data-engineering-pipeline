from src.ingestion.ingestion_manager import ingest
path="C:\EnterpriseDataSources\olist_sellers_dataset.csv"


def main():

    df = ingest(
        source_type="csv",
        source=path
    )

    print("=" * 60)
    print("INGESTION MANAGER TEST")
    print("=" * 60)

    print(df.head())

    print("\nShape:", df.shape)


if __name__ == "__main__":
    main()