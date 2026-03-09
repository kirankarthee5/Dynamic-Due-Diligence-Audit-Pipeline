import sqlite3
import pandas as pd
import time

print('Starting...')
start_time=time.time()

df_trades=pd.read_csv('Raw_Gen.csv')
conn=sqlite3.connect('Raw_Database.db')

df_trades.to_sql('Trades',conn,index=False)

cursor=conn.cursor()
cursor.executescript('''CREATE TABLE Firms ('Firm_ID','Firm_Name','Risk_lvl')''')

firms_data = [
    (101, 'Reliance Ltd.', 'Low Risk'),
    (102, 'Adani Ent.', 'Medium Risk'),
    (103, 'Aditya Birla', 'High Risk'),
    (104, 'Palantir', 'High Risk'),
    (105, 'Tata & Sons', 'Low Risk')
]
cursor.executemany('INSERT INTO Firms VALUES (?,?,?)', firms_data)

conn.commit()
conn.close()

end_time=time.time()
print('Success...')
