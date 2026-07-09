from src.ingestion.csv_ingestion import read_csv
path="C:\Users\TEJ\OneDrive\Desktop\EnterpriseDataSources\CRM\geolocation.csv"

df = read_csv(path)

print("\nData Preview:")
print(df.head())

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())