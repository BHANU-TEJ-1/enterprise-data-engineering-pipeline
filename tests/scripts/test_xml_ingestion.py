from src.ingestion.xml_ingestion import read_xml


def main():

    df = read_xml("data/source/xml/products.xml")

    print("=" * 60)
    print("XML INGESTION TEST")
    print("=" * 60)

    print(df.head())

    print("\nShape:", df.shape)
    print("\nColumns:", list(df.columns))
    print("\nDtypes:\n", df.dtypes)


if __name__ == "__main__":
    main()