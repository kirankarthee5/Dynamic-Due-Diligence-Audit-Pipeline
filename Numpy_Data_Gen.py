import numpy as np
import csv
import time

print('Starting...')
start_time=time.time()

Total_Trades=100000

trade_ID=np.arange(1,Total_Trades +1)

firm_id=np.random.choice([101,102,103,104,105], size=Total_Trades)

amount=np.random.normal(loc=50000,scale=15000,size=Total_Trades)
amount=np.round(amount,2)

status=np.random.choice(['PASS','FAIL'], size=Total_Trades,p=[0.90,0.10])

#CSV
with open ('Raw_Gen.csv','w',newline='') as file:
    writer= csv.writer(file)
    writer.writerow(['Trade_ID','Firm_ID','Amount','Status'])
    
    writer.writerows(zip(trade_ID,firm_id,amount,status))

end_time=time.time()
print('Success!')
    