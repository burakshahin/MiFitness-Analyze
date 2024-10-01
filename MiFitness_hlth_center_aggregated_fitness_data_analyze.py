import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the data
data = '''timestamp	avg_hr	sleep_score	total_duration	deep_sleep_duration	light_sleep_duration	rem_sleep_duration	awake_count
1677715200	60	82	454	153	197	104	2
1677801600	60	85	492	171	191	130	1
1677888000	63	77	513	175	252	51	0
'''

# Convert the data into a DataFrame
from io import StringIO
df = pd.read_csv(StringIO(data), sep='\t')

# Convert timestamp to datetime
df['date'] = pd.to_datetime(df['timestamp'], unit='s')

# Set the date as the index
df.set_index('date', inplace=True)

# Basic Statistics
print("Basic Statistics:")
print(df.describe())

# Plotting average heart rate over time
plt.figure(figsize=(12, 6))
plt.plot(df.index, df['avg_hr'], label='Average Heart Rate', color='blue')
plt.title('Average Heart Rate Over Time')
plt.xlabel('Date')
plt.ylabel('Average Heart Rate (bpm)')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

# Plotting sleep score over time
plt.figure(figsize=(12, 6))
plt.plot(df.index, df['sleep_score'], label='Sleep Score', color='orange')
plt.title('Sleep Score Over Time')
plt.xlabel('Date')
plt.ylabel('Sleep Score')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

# Correlation Heatmap
plt.figure(figsize=(10, 6))
correlation = df[['avg_hr', 'sleep_score', 'total_duration', 'deep_sleep_duration', 
                  'light_sleep_duration', 'rem_sleep_duration', 'awake_count']].corr()
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()

# Plotting the total sleep duration
plt.figure(figsize=(12, 6))
plt.plot(df.index, df['total_duration']/60, marker='o', linestyle='-', color='b')

plt.title('Total Sleep Duration Over Time')
plt.xlabel('Date')
plt.ylabel('Total Sleep Duration (hours)')
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.show()

# Calculate average sleep hours
df['average_sleep_hours'] = df['total_duration'].rolling(window=7).mean() / 60  # 7-day rolling average in hours

# Plotting total sleep duration and average sleep hours
plt.figure(figsize=(12, 6))

# Plot total sleep duration in hours
plt.plot(df.index, df['total_duration'] / 60, marker='o', linestyle='-', color='b', label='Total Sleep Duration (hours)')

# Plot average sleep hours
plt.plot(df.index, df['average_sleep_hours'], marker='x', linestyle='--', color='orange', label='Average Sleep Hours')

plt.title('Total Sleep Duration and Average Sleep Hours Over Time')
plt.xlabel('Date')
plt.ylabel('Sleep Duration (hours)')
plt.xticks(rotation=45)
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()

# Calculate the moving average for total sleep duration and average sleep hours
window_size = 7  # You can change this to any number of days you prefer

# Moving averages
df['moving_avg_duration'] = df['total_duration'].rolling(window=window_size).mean() / 60  # Total duration in hours
df['moving_avg_average_sleep'] = df['average_sleep_hours'].rolling(window=window_size).mean()  # Average sleep hours

# Plotting the moving averages
plt.figure(figsize=(12, 6))

# Plot moving average of total sleep duration in hours
plt.plot(df.index, df['moving_avg_duration'], marker='o', linestyle='-', color='b', label='Moving Average Total Sleep Duration (hours)')

# Plot moving average of average sleep hours
plt.plot(df.index, df['moving_avg_average_sleep'], marker='x', linestyle='--', color='orange', label='Moving Average Average Sleep Hours')

plt.title('Moving Averages of Total Sleep Duration and Average Sleep Hours Over Time')
plt.xlabel('Date')
plt.ylabel('Sleep Duration (hours)')
plt.xticks(rotation=45)
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()
