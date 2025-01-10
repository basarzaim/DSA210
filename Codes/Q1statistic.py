import pandas as pd
from scipy import stats

# Load the data (replace with actual file paths)
spotify_data = pd.read_csv("spotify_data_with_genres.csv")
calories_burned_data = pd.read_csv("HKQuantityTypeIdentifierActiveEnergyBurned_filtered.csv")

# Preprocessing Spotify Data
spotify_data['ts'] = pd.to_datetime(spotify_data['ts'])
spotify_data['date'] = spotify_data['ts'].dt.date

# Map genres
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
}
spotify_data['broad_genre'] = spotify_data['genre'].map(genre_mapping).fillna('Other')

# Calculate listening time
spotify_data['listening_time_minutes'] = spotify_data['ms_played'] / 60000

# Aggregate Spotify data by date and genre
daily_listening = (
    spotify_data.groupby(['date', 'broad_genre'])['listening_time_minutes']
    .sum()
    .reset_index()
)

# Preprocessing Calories Burned Data
calories_burned_data['startDate'] = pd.to_datetime(calories_burned_data['startDate'])
calories_burned_data['date'] = calories_burned_data['startDate'].dt.date

# Aggregate Calories Burned by Date
daily_calories = (
    calories_burned_data.groupby('date')['value']
    .sum()
    .reset_index()
    .rename(columns={'value': 'calories_burned'})
)

# Merge the data
combined_data = daily_listening.merge(daily_calories, on='date', how='inner')

# Check for issues in the calories_burned column
print("Calories Burned Statistics:")
print(combined_data['calories_burned'].describe())

# Drop or replace negative or NaN values
combined_data = combined_data[combined_data['calories_burned'] >= 0]
combined_data['calories_burned'] = combined_data['calories_burned'].fillna(0)

# Create bins dynamically
max_calories = combined_data['calories_burned'].max()
# Define bins dynamically based on the dataset
bins = [0, 160, 281, 451, 700]  # Adjusted to align with min, 25th, 50th, 75th percentiles, and max
labels = ['Low', 'Medium', 'High', 'Very High']

# Categorize calories burned into bins
combined_data['activity_level'] = pd.cut(combined_data['calories_burned'], bins=bins, labels=labels, right=False)

# Create a contingency table
contingency_table = pd.crosstab(combined_data['broad_genre'], combined_data['activity_level'])

# Perform Chi-Square Test
chi2, p, dof, expected = stats.chi2_contingency(contingency_table)

# Print Results
print("\nChi-Square Test Results:")
print(f"Chi-Square Statistic: {chi2}")
print(f"P-value: {p}")
print(f"Degrees of Freedom: {dof}")
print("\nExpected Frequencies Table:")
print(expected)
