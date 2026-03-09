import pandas as pd
import sqlite3
import time

print('Beginning...')
start_time=time.time()

conn=sqlite3.connect('Raw_Database.db')

query = """
SELECT Firms.Firm_Name, Firms.Risk_lvl, Trades.Amount, Trades.Status
FROM Trades
JOIN Firms ON Trades.Firm_ID = Firms.Firm_ID"""

df=pd.read_sql_query(query,conn)
conn.commit()
conn.close()

print("Calculating Risk Exposure...")
failed_trades = df[df['Status'] == 'FAIL']

risk_summary = failed_trades.groupby(['Firm_Name', 'Risk_lvl'])['Amount'].sum().reset_index()

risk_summary['Exposure (Millions INR)'] = (risk_summary['Amount'] / 1000000).round(2)

risk_summary = risk_summary.sort_values(by='Exposure (Millions INR)', ascending=False)

risk_summary.to_csv('Executive_Risk_Report.csv', index=False)

end_time = time.time()
print(f"✅ Audit Complete in {round(end_time - start_time, 3)} seconds.")