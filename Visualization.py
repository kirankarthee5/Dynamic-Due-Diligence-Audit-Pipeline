import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('Executive_Risk_Report.csv')
plt.figure(figsize=(10, 6))
sns.set_theme(style="whitegrid")

chart = sns.barplot('''
x='Firm_Name', 
y='Exposure (Millions INR)', 
hue='Risk_Profile', 
data=df, 
palette='Reds_r'
''')

plt.title('Dynamic Due Diligence: Total Risk Exposure by Firm', fontsize=16, fontweight='bold')
plt.xlabel('Brokerage Firm', fontsize=12)
plt.ylabel('Financial Exposure (Millions INR)', fontsize=12)

plt.tight_layout()
plt.savefig('Boardroom_Dashboard.png', dpi=300) # dpi=300 makes it high-res
print("✅ SUCCESS: 'Boardroom_Dashboard.png' has been created!")
plt.show()