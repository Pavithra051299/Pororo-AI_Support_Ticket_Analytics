import pandas as pd
import psycopg2

# Load cleaned dataset
df = pd.read_csv("C:/Users/Pavithra/Pororo/data/cleaned_support_tickets.csv")
df = df.where(pd.notnull(df), None)

df["date_of_purchase"] = pd.to_datetime(df["date_of_purchase"], errors="coerce")
df["first_response_time"] = pd.to_datetime(df["first_response_time"], errors="coerce")
df["time_to_resolution"] = pd.to_datetime(df["time_to_resolution"], errors="coerce")
df = df.astype(object).where(pd.notnull(df), None)

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="PororoDB",
    user="postgres",
    password="Pororo"
)

cursor = conn.cursor()

# Insert data
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO tickets VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """, tuple(row))

conn.commit()

print("Data successfully loaded!")

cursor.close()
conn.close()