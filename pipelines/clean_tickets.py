import pandas as pd

# Load dataset
df = pd.read_csv("C:/Users/Pavithra/Pororo/data/customer_support_tickets.csv")

# Normalize column names
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

# Drop rows with no ticket description
df = df.dropna(subset=["ticket_description"])

# Standardize ticket priority
df["ticket_priority"] = df["ticket_priority"].str.capitalize()

# Convert purchase date to datetime
df["date_of_purchase"] = pd.to_datetime(df["date_of_purchase"], errors="coerce")

print("Cleaned column names:\n")
print(df.columns)

print("\nPreview of dataset:")
print(df.head())

print("\nMissing values per column:\n")
print(df.isnull().sum())

df.to_csv("C:/Users/Pavithra/Pororo/data/cleaned_support_tickets.csv", index=False)

print("\nCleaned dataset saved.")