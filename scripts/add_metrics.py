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


query = """
SELECT 
    p_date, client_name, cost, clicks, impressions, sales, gmv
FROM campaign_performance
"""
df = pd.read_sql(query, conn)

# Calculate new metrics
df['ctr'] = (df['clicks'] / df['impressions']) * 100
df['conversion_rate'] = (df['sales'] / df['clicks']) * 100
df['roi'] = ((df['gmv'] * 0.20 - df['cost']) / df['cost']) * 100
df['cpa'] = df['cost'] / df['sales']

# Adding new column to the database
for _, row in df.iterrows():
    values = (
        row["p_date"], row["client_name"], row["cost"], row["clicks"], row["impressions"],
        row["sales"], row["gmv"], row["ctr"], row["conversion_rate"], row["roi"], row["cpa"]
    )
    
    cursor.execute("""
        UPDATE campaign_performance
        SET ctr = %s, conversion_rate = %s, roi = %s, cpa = %s
        WHERE p_date = %s AND client_name = %s
    """, values[7:] + values[:2]) 

conn.commit()
cursor.close()
conn.close()

print(df[['p_date', 'client_name', 'ctr', 'conversion_rate', 'roi', 'cpa']].head())
