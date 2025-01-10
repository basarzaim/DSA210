import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

# Load data
spotify_data = pd.read_csv('spotify_data_with_genres.csv')
walking_speed_data = pd.read_csv('HKQuantityTypeIdentifierWalkingSpeed_filtered.csv')
walking_asymmetry_data = pd.read_csv('HKQuantityTypeIdentifierWalkingAsymmetryPercentage_filtered.csv')

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

spotify_data['broad_genre'] = spotify_data['genre'].apply(map_genre)

# Calculate listening time in minutes
spotify_data['listening_time_minutes'] = spotify_data['ms_played'] / 60000  # Convert ms to minutes

# Aggregate listening time per genre per day
daily_listening = (
    spotify_data.groupby(['date', 'broad_genre'])['listening_time_minutes']
    .sum()
    .reset_index()
)

# Filter prolonged listening days
PROLONGED_THRESHOLD = 30
prolonged_listening = daily_listening[daily_listening['listening_time_minutes'] >= PROLONGED_THRESHOLD]

# Calculate daily average prolonged listening time
average_prolonged = (
    prolonged_listening.groupby('date')['listening_time_minutes']
    .mean()
    .reset_index()
    .rename(columns={'listening_time_minutes': 'Avg_Prolonged_Listening'})
)

# Categorize days based on average prolonged listening
bins = [0, 60, 90, 120, float('inf')]
labels = ['<60 min', '60-90 min', '90-120 min', '>120 min']
average_prolonged['Listening_Category'] = pd.cut(
    average_prolonged['Avg_Prolonged_Listening'], bins=bins, labels=labels, right=False
)

# Preprocess walking metrics
walking_speed_data['startDate'] = pd.to_datetime(walking_speed_data['startDate'])
walking_asymmetry_data['startDate'] = pd.to_datetime(walking_asymmetry_data['startDate'])

walking_speed_data['date'] = walking_speed_data['startDate'].dt.date
walking_asymmetry_data['date'] = walking_asymmetry_data['startDate'].dt.date

# Aggregate walking metrics by day
walking_metrics = (
    walking_speed_data.groupby('date')['value']
    .mean()
    .reset_index()
    .rename(columns={'value': 'Avg_Walking_Speed'})
    .merge(
        walking_asymmetry_data.groupby('date')['value']
        .mean()
        .reset_index()
        .rename(columns={'value': 'Avg_Walking_Asymmetry'}),
        on='date'
    )
)

# Merge listening categories with walking metrics
combined_data = average_prolonged.merge(walking_metrics, on='date', how='inner')

# ANOVA Test for Walking Speed
anova_speed = stats.f_oneway(
    *[group['Avg_Walking_Speed'].dropna() for _, group in combined_data.groupby('Listening_Category')]
)
print("\nANOVA Test for Walking Speed:")
print(f"F-Statistic: {anova_speed.statistic}, P-Value: {anova_speed.pvalue}")

# ANOVA Test for Walking Asymmetry
anova_asymmetry = stats.f_oneway(
    *[group['Avg_Walking_Asymmetry'].dropna() for _, group in combined_data.groupby('Listening_Category')]
)
print("\nANOVA Test for Walking Asymmetry:")
print(f"F-Statistic: {anova_asymmetry.statistic}, P-Value: {anova_asymmetry.pvalue}")

# Boxplot: Walking Speed by Listening Category
plt.figure(figsize=(12, 6))
sns.boxplot(
    x='Listening_Category',
    y='Avg_Walking_Speed',
    data=combined_data,
    palette='Set2'
)
plt.title('Walking Speed by Average Prolonged Listening Category')
plt.xlabel('Prolonged Listening Category')
plt.ylabel('Average Walking Speed (m/s)')
plt.tight_layout()
plt.show()

# Boxplot: Walking Asymmetry by Listening Category
plt.figure(figsize=(12, 6))
sns.boxplot(
    x='Listening_Category',
    y='Avg_Walking_Asymmetry',
    data=combined_data,
    palette='Set3'
)
plt.title('Walking Asymmetry by Average Prolonged Listening Category')
plt.xlabel('Prolonged Listening Category')
plt.ylabel('Average Walking Asymmetry (%)')
plt.tight_layout()
plt.show()
