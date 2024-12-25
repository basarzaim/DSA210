import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the CSV data
spotify_data = pd.read_csv('spotify_data_with_genres.csv')
calories_burned_data = pd.read_csv('HKQuantityTypeIdentifierActiveEnergyBurned_filtered.csv')
distance_walked_data = pd.read_csv('HKQuantityTypeIdentifierDistanceWalkingRunning_filtered.csv')

# Define a mapping of subgenres to broader genres
genre_mapping = {
    'german metal': 'Metal',
    'german power metal': 'Metal',
    'hard rock': 'Rock',
    'metal': 'Metal',
    'alternative metal': 'Metal',
    'album rock': 'Rock',
    'birmingham metal': 'Metal',
    'nu metal': 'Metal',
    'wrestling': 'Sports',
    'pop': 'Pop',
    'dance pop': 'Pop',
    'indie pop': 'Indie',
    'country': 'Country',
    'edm': 'Electronic',
    # Add more mappings here for other subgenres
}

def map_genre(subgenre):
    for key, value in genre_mapping.items():
        if isinstance(subgenre, str) and key in subgenre:
            return value
    return 'Other'  # Default category for unmapped genres

# Apply the mapping to the Spotify data
spotify_data['broad_genre'] = spotify_data['genre'].apply(map_genre)

# Preprocess the data for monthly analysis
spotify_data['ts'] = pd.to_datetime(spotify_data['ts'])
calories_burned_data['startDate'] = pd.to_datetime(calories_burned_data['startDate'])
distance_walked_data['startDate'] = pd.to_datetime(distance_walked_data['startDate'])

# Add a 'month' column to group by month
spotify_data['month'] = spotify_data['ts'].dt.to_period('M')
calories_burned_data['month'] = calories_burned_data['startDate'].dt.to_period('M')
distance_walked_data['month'] = distance_walked_data['startDate'].dt.to_period('M')

# Aggregate Spotify data: Total listening time per genre per month
spotify_data['ms_played_minutes'] = spotify_data['ms_played'] / 60000  # Convert ms to minutes
spotify_monthly = (
    spotify_data.groupby(['month', 'broad_genre'])['ms_played_minutes']
    .sum()
    .reset_index()
    .rename(columns={'ms_played_minutes': 'total_listening_time'})
)

# Aggregate health data: Average calories burned and step count per month
calories_monthly = (
    calories_burned_data.groupby('month')['value']
    .mean()
    .reset_index()
    .rename(columns={'value': 'avg_calories_burned'})
)
steps_monthly = (
    distance_walked_data.groupby('month')['value']
    .mean()
    .reset_index()
    .rename(columns={'value': 'avg_step_count'})
)

# Merge aggregated data
spotify_monthly = spotify_monthly.merge(
    steps_monthly, on='month', how='left'
).merge(
    calories_monthly, on='month', how='left'
)

# Calculate weighted averages for steps and calories burned
spotify_monthly['weighted_step_count'] = (
    spotify_monthly['total_listening_time'] * spotify_monthly['avg_step_count']
)
spotify_monthly['weighted_calories_burned'] = (
    spotify_monthly['total_listening_time'] * spotify_monthly['avg_calories_burned']
)

# Create pivot tables for visualization
pivoted_steps = spotify_monthly.pivot(index='month', columns='broad_genre', values='weighted_step_count').fillna(0)
pivoted_calories = spotify_monthly.pivot(index='month', columns='broad_genre', values='weighted_calories_burned').fillna(0)

# Stacked Bar Chart: Step Count
plt.figure(figsize=(14, 7))
pivoted_steps.plot(kind='bar', stacked=True, figsize=(14, 7), colormap='tab10')
plt.title("Monthly Weighted Step Count by Genre (Stacked)")
plt.xlabel("Month")
plt.ylabel("Weighted Step Count")
plt.legend(title="Genre", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# Stacked Bar Chart: Calories Burned
plt.figure(figsize=(14, 7))
pivoted_calories.plot(kind='bar', stacked=True, figsize=(14, 7), colormap='tab10')
plt.title("Monthly Weighted Calories Burned by Genre (Stacked)")
plt.xlabel("Month")
plt.ylabel("Weighted Calories Burned")
plt.legend(title="Genre", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

