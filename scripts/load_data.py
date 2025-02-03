import pandas as pd
import mysql.connector

# Connect to MySQL Database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="client_metrics_db"
)
cursor = conn.cursor()

# Load dataset to DataFrame
df = pd.read_csv('data/campaign_performance.csv', sep=';', header=0)
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

df["p_date"] = pd.to_datetime(df["p_date"], format="%d/%m/%Y").dt.date
df["cost"] = df["cost_(usd)"].replace('[\$,]', '', regex=True).astype(float)
df["gmv"] = df["gmv"].replace('[\$,]', '', regex=True).astype(float)
df["impressions"] = df["impressions"].replace('[\.,]', '', regex=True).astype(int)
df["clicks"] = df["clicks"].replace('[\.,]', '', regex=True).astype(int)
df["sales"] = df["sales"].astype(int)

df.drop(columns=["cost_(usd)"], inplace=True)

# Insert data to MySQL
for _, row in df.iterrows():
    values = (
        row["p_date"], row["client_name"], row["cost"],
        row["clicks"], row["impressions"], row["sales"], row["gmv"]
    )

    cursor.execute("""
        INSERT INTO campaign_performance (p_date, client_name, cost, clicks, impressions, sales, gmv)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, values)

conn.commit()
cursor.close()
conn.close()