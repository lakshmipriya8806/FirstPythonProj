import requests
import json
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import os



# Calculate dates
today = datetime.now()
week_ago = today - timedelta(days=5)

# Format dates for API (YYYY-MM-DD)
start_date = week_ago.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")

# Get Paris weather for past week
url = f"https://api.open-meteo.com/v1/forecast?latitude=48.85&longitude=2.35&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"

response = requests.get(url)
data = response.json()
print(json.dumps(data,indent=4))

#today_temp=data["daily"]["time[0]"]

#print(today_temp)
# Extract the daily data
daily_data = data['daily']

# Create a DataFrame
df = pd.DataFrame({
    'date': daily_data['time'],
    'high_temp': daily_data['temperature_2m_max'],
    'low_temp': daily_data['temperature_2m_min']
})

# Convert date strings to datetime
#df['date'] = pd.to_datetime(df['date'])

print(df)


# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(df['date'], df['high_temp'], marker='*', label='Max Temp')
plt.plot(df['date'], df['low_temp'], marker='*', label='Min Temp')

# Add labels and title
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('NYC Weather - Past 5 Days')
plt.legend()

# Rotate x-axis labels for readability
plt.xticks(rotation=50)
plt.tight_layout()

# Save the plot
plt.savefig('nycweather.png')
plt.show()


# Create data folder if it doesn't exist
if not os.path.exists('weather'):
    os.makedirs('weather')

# Save to CSV
df.to_csv('weather/nycweather.csv', index=False)
print("Data saved to weather/nycweather.csv")