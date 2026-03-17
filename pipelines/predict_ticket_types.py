# pipelines/predict_ticket_types.py

import psycopg2
import pandas as pd
import joblib
from scipy.sparse import hstack

# -----------------------------
# 1. Connect to PostgreSQL
# -----------------------------
conn = psycopg2.connect(
    host="localhost",
    database="PororoDB",
    user="postgres",
    password="Pororo"
)

# -----------------------------
# 2. Load tickets from database
# -----------------------------
query = """
SELECT 
ticket_id,
ticket_subject,
ticket_description,
ticket_priority,
ticket_channel,
product_purchased,
ticket_type
FROM tickets
"""

df = pd.read_sql(query, conn)

print("Loaded tickets:", df.shape)

# -----------------------------
# 3. Load trained AI components
# -----------------------------
model = joblib.load("../ai_models/ticket_classifier.pkl")
vectorizer = joblib.load("../ai_models/tfidf_vectorizer.pkl")
encoder = joblib.load("../ai_models/feature_encoder.pkl")

# -----------------------------
# 4. Preprocess text
# -----------------------------
df["text"] = df["ticket_subject"].astype(str) + " " + df["ticket_description"].astype(str)

text_features = vectorizer.transform(df["text"])

# -----------------------------
# 5. Structured features
# -----------------------------
structured = df[
    ["ticket_priority", "ticket_channel", "product_purchased"]
].astype(str)

encoded_structured = encoder.transform(structured)

# -----------------------------
# 6. Combine features
# -----------------------------
X = hstack([text_features, encoded_structured])

# -----------------------------
# 7. Predict ticket type
# -----------------------------
predictions = model.predict(X)

df["predicted_ticket_type"] = predictions

print(df[["ticket_id", "predicted_ticket_type"]].head())

# -----------------------------
# 8. Create prediction table
# -----------------------------
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS ticket_predictions (
ticket_id INT,
actual_ticket_type TEXT,
predicted_ticket_type TEXT
)
""")

conn.commit()

# -----------------------------
# 9. Insert predictions
# -----------------------------
for _, row in df.iterrows():
    cursor.execute("""
    INSERT INTO ticket_predictions
    (ticket_id, actual_ticket_type, predicted_ticket_type)
    VALUES (%s, %s, %s)
    """, (
        int(row["ticket_id"]),
        row["ticket_type"],
        row["predicted_ticket_type"]
    ))

conn.commit()

print("Predictions stored in database")

cursor.close()
conn.close()