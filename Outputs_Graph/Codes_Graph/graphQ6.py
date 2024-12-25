import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
spotify_data = pd.read_csv('spotify_data_with_genres.csv')
headphone_audio_data = pd.read_csv('HKQuantityTypeIdentifierHeadphoneAudioExposure_filtered.csv')

# Preprocess Spotify data
spotify_data['ts'] = pd.to_datetime(spotify_data['ts'])
spotify_data['date'] = spotify_data['ts'].dt.date  # Extract date

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

# Calculate listening time in minutes
spotify_data['listening_time_minutes'] = spotify_data['ms_played'] / 60000  # Convert ms to minutes

# Aggregate Spotify data by date and genre
daily_listening = (
    spotify_data.groupby(['date', 'broad_genre'])['listening_time_minutes']
    .sum()
    .reset_index()
)

# Preprocess headphone audio data
headphone_audio_data['startDate'] = pd.to_datetime(headphone_audio_data['startDate'])
headphone_audio_data['date'] = headphone_audio_data['startDate'].dt.date  # Extract date

# Aggregate headphone audio data by date
daily_audio_exposure = (
    headphone_audio_data.groupby('date')['value']
    .mean()
    .reset_index()
    .rename(columns={'value': 'Avg_Audio_Exposure'})
)

# Merge listening and audio data
combined_data = daily_listening.merge(daily_audio_exposure, on='date', how='inner')

# Bar Plot: Mean Audio Exposure by Genre
plt.figure(figsize=(12, 6))
sns.barplot(
    x='broad_genre',
    y='Avg_Audio_Exposure',
    data=combined_data,
    ci='sd',  # Show standard deviation as error bars
    palette='Set2'
)
plt.title('Mean Headphone Audio Exposure by Music Genre')
plt.xlabel('Music Genre')
plt.ylabel('Average Audio Exposure (dB)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
