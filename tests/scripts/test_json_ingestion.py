from src.ingestion.json_ingestion import read_json

path="C:\EnterpriseDataSources\OMS\orders.json"
def main():

    df = read_json(path)

    print("=" * 60)
    print("JSON INGESTION TEST")
    print("=" * 60)

    print(df.head())

    print("\nShape:", df.shape)
    print("\nColumns:", list(df.columns))
    print("\nDtypes:\n", df.dtypes)


if __name__ == "__main__":
    main()