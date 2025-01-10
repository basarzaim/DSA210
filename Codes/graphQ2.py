import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV data
spotify_data = pd.read_csv('spotify_data_with_genres.csv')
calories_burned_data = pd.read_csv('HKQuantityTypeIdentifierActiveEnergyBurned_filtered.csv')
distance_walked_data = pd.read_csv('HKQuantityTypeIdentifierDistanceWalkingRunning_filtered.csv')

# Preprocess the data
spotify_data['ts'] = pd.to_datetime(spotify_data['ts'])
calories_burned_data['startDate'] = pd.to_datetime(calories_burned_data['startDate'])
distance_walked_data['startDate'] = pd.to_datetime(distance_walked_data['startDate'])

# Aggregate Spotify data by daily listening time
spotify_data['listening_time_minutes'] = spotify_data['ms_played'] / 60000  # Convert ms to minutes
daily_listening = (
    spotify_data.groupby(spotify_data['ts'].dt.date)['listening_time_minutes']
    .sum()
    .reset_index()
    .rename(columns={'ts': 'Date', 'listening_time_minutes': 'Total_Listening_Time'})
)

# Aggregate exercise data by daily calories burned and steps
daily_calories = (
    calories_burned_data.groupby(calories_burned_data['startDate'].dt.date)['value']
    .sum()
    .reset_index()
    .rename(columns={'startDate': 'Date', 'value': 'Total_Calories_Burned'})
)
daily_steps = (
    distance_walked_data.groupby(distance_walked_data['startDate'].dt.date)['value']
    .sum()
    .reset_index()
    .rename(columns={'startDate': 'Date', 'value': 'Total_Steps'})
)

# Merge the datasets on the Date column
daily_data = (
    daily_listening.merge(daily_calories, on='Date', how='inner')
    .merge(daily_steps, on='Date', how='inner')
)

# Calculate exercise intensity metrics
daily_data['Calories_per_Minute'] = daily_data['Total_Calories_Burned'] / daily_data['Total_Listening_Time']
daily_data['Steps_per_Minute'] = daily_data['Total_Steps'] / daily_data['Total_Listening_Time']

# Filter out rows with near-zero and extremely high values
filtered_data = daily_data[
    (daily_data['Total_Listening_Time'] > 5) &
    (daily_data['Total_Listening_Time'] < 1000) &  # Upper limit for listening time
    (daily_data['Calories_per_Minute'] > 0.1) &
    (daily_data['Calories_per_Minute'] < 50) &  # Upper limit for calories per minute
    (daily_data['Steps_per_Minute'] > 0.1) &
    (daily_data['Steps_per_Minute'] < 200)  # Upper limit for steps per minute
]

# Scatter Plot: Steps per Minute vs Listening Time (Filtered Daily Data)
plt.figure(figsize=(10, 6))
sns.regplot(
    x='Total_Listening_Time',
    y='Steps_per_Minute',
    data=filtered_data,
    color='blue',
    line_kws={"linewidth": 2},
    scatter_kws={"alpha": 0.6}
)
plt.title('Steps per Minute vs Listening Time (Filtered Daily Data)')
plt.xlabel('Total Listening Time (minutes)')
plt.ylabel('Steps per Minute')
plt.tight_layout()
plt.show()

# Scatter Plot: Calories Burned per Minute vs Listening Time (Filtered Daily Data)
plt.figure(figsize=(10, 6))
sns.regplot(
    x='Total_Listening_Time',
    y='Calories_per_Minute',
    data=filtered_data,
    color='red',
    line_kws={"linewidth": 2},
    scatter_kws={"alpha": 0.6}
)
plt.title('Calories Burned per Minute vs Listening Time (Filtered Daily Data)')
plt.xlabel('Total Listening Time (minutes)')
plt.ylabel('Calories Burned per Minute')
plt.tight_layout()
plt.show()
