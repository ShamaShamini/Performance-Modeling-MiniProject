import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# -------------------------------
# Load the dataset
# -------------------------------
data = pd.read_excel(r"C:\Users\HP\Downloads\ATM_Dataset.xlsx")

# Convert Date + Time into one datetime column
data['DateTime'] = pd.to_datetime(data['Date'] + ' ' + data['Time'])

# -------------------------------
# Waiting Time Calculation
# -------------------------------
data = data.sort_values(by=['DateTime', 'Arrival_Time_Min']).reset_index(drop=True)
data['Service_Start_Min'] = data['Arrival_Time_Min']

for i in range(1, len(data)):
    prev_end = (
        data.loc[i-1, 'Service_Start_Min']
        + data.loc[i-1, 'Service_Time_Min']
        + data.loc[i-1, 'Downtime_Duration_Min']
    )
    data.loc[i, 'Service_Start_Min'] = max(data.loc[i, 'Arrival_Time_Min'], prev_end)

data['Waiting_Time_Min'] = data['Service_Start_Min'] - data['Arrival_Time_Min']

# Split into peak / off peak
peak_data = data[data['Period'] == 'Peak']
off_peak_data = data[data['Period'] == 'Off-Peak']

# -------------------------------
# 1. Histogram of Waiting Times
# -------------------------------
plt.figure(figsize=(10, 6))
sns.histplot(data['Waiting_Time_Min'], bins=30, kde=True, color='blue', label='All Periods')
sns.histplot(peak_data['Waiting_Time_Min'], bins=30, kde=True, color='red', alpha=0.5, label='Peak')
sns.histplot(off_peak_data['Waiting_Time_Min'], bins=30, kde=True, color='green', alpha=0.5, label='Off-Peak')
plt.title('Distribution of Waiting Times')
plt.xlabel('Waiting Time (Minutes)')
plt.ylabel('Frequency')
plt.legend()
plt.show()

# -------------------------------
# 2. Queue Length Over Time
# -------------------------------
plt.figure(figsize=(12, 6))
plt.plot(data['DateTime'], data['Queue_Length'], color='purple', label='Queue Length')
plt.title('Queue Length Over Time')
plt.xlabel('Time')
plt.ylabel('Queue Length')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

# -------------------------------
# 3. Transaction Type Analysis (Side-by-side Bar Chart)
# -------------------------------
transaction_summary = data.groupby('Transaction_Type').agg(
    Avg_Service_Time=('Service_Time_Min', 'mean'),
    Count=('Transaction_Type', 'count')
).reset_index()

x = np.arange(len(transaction_summary['Transaction_Type']))
width = 0.4

plt.figure(figsize=(12, 6))
plt.bar(x - width/2, transaction_summary['Avg_Service_Time'], width, label='Avg Service Time')
plt.bar(x + width/2, transaction_summary['Count'], width, label='Transaction Count')

plt.xticks(x, transaction_summary['Transaction_Type'])
plt.title('Average Service Time and Count by Transaction Type')
plt.xlabel('Transaction Type')
plt.ylabel('Value')
plt.legend()
plt.show()

# -------------------------------
# 4. Downtime Impact on Queue Length
# -------------------------------
plt.figure(figsize=(10, 6))
sns.boxplot(x='Downtime_Event', y='Queue_Length', data=data)
plt.title('Queue Length: Downtime vs No Downtime')
plt.xlabel('Downtime Event')
plt.ylabel('Queue Length')
plt.xticks([0, 1], ['No Downtime', 'Downtime'])
plt.show()
