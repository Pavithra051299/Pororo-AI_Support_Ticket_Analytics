import pandas as pd

df = pd.read_csv("C:/Users/Pavithra/Pororo/data/customer_support_tickets.csv")

print(df.head())
print("\nColumns:")
print(df.columns)

print("\nDataset Info:")
print(df.info())

print("\nMissing values:")
print(df.isnull().sum())