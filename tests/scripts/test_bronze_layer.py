from src.bronze.bronze_layer import BronzeLayer
from src.ingestion.csv_ingestion import read_csv


def main():

    df = read_csv("C:/Users/TEJ/OneDrive/Desktop/EnterpriseDataSources/CRM/customers.csv")

    bronze = BronzeLayer()

    bronze.write_parquet(
                          df,
                          "customers")

    print("\nBronze layer test completed successfully.")


if __name__ == "__main__":
    main()