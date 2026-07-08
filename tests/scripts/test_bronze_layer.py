from src.bronze.bronze_layer import write_to_bronze
from src.ingestion.csv_ingestion import read_csv


def main():

    df = read_csv("C:/Users/TEJ/OneDrive/Desktop/EnterpriseDataSources/CRM/customers.csv")

    write_to_bronze(
        dataframe=df,
        dataset_name="customers"
    )

    print("\nBronze layer test completed successfully.")


if __name__ == "__main__":
    main()