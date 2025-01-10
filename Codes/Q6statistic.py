import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import f_oneway

# Load data
spotify_data = pd.read_csv('spotify_data_with_genres.csv')
audio_exposure_data = pd.read_csv('HKQuantityTypeIdentifierHeadphoneAudioExposure_filtered.csv')

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

def map_genre(subgenre):
    for key, value in genre_mapping.items():
        if isinstance(subgenre, str) and key in subgenre:
            return value
    return 'Other'  # Default category for unmapped genres

# Apply the mapping to the Spotify data
spotify_data['broad_genre'] = spotify_data['genre'].apply(map_genre)

# Aggregate listening time per genre per day
daily_listening = (
    spotify_data.groupby(['date', 'broad_genre'])['ms_played']
    .sum()
    .reset_index()
    .rename(columns={'ms_played': 'total_listening_time_ms'})
)

# Convert listening time to minutes
daily_listening['total_listening_time_minutes'] = daily_listening['total_listening_time_ms'] / 60000

# Preprocess Audio Exposure Data
audio_exposure_data['startDate'] = pd.to_datetime(audio_exposure_data['startDate'])
audio_exposure_data['date'] = audio_exposure_data['startDate'].dt.date

# Aggregate audio exposure by day
daily_audio_exposure = (
    audio_exposure_data.groupby('date')['value']
    .mean()
    .reset_index()
    .rename(columns={'value': 'Avg_Audio_Exposure'})
)

# Merge listening data with audio exposure data
combined_data = daily_listening.merge(daily_audio_exposure, on='date', how='inner')

# Descriptive Statistics
descriptive_stats = combined_data.groupby('broad_genre')['Avg_Audio_Exposure'].describe()
print("Descriptive Statistics for Audio Exposure by Genre:")
print(descriptive_stats)

# Perform ANOVA Test
anova_results = f_oneway(
    *[group['Avg_Audio_Exposure'].dropna() for _, group in combined_data.groupby('broad_genre')]
)
print("\nANOVA Test Results:")
print(f"F-Statistic: {anova_results.statistic}, P-Value: {anova_results.pvalue}")

# Visualization
plt.figure(figsize=(12, 6))
sns.boxplot(
    x='broad_genre',
    y='Avg_Audio_Exposure',
    data=combined_data,
    palette='Set3'
)
plt.title('Headphone Audio Exposure by Music Genre')
plt.xlabel('Music Genre')
plt.ylabel('Average Headphone Audio Exposure (dB)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
