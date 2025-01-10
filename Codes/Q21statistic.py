import pandas as pd
import numpy as np
import statsmodels.api as sm
from scipy.stats import pearsonr
import matplotlib.pyplot as plt

# Load data
spotify_data = pd.read_csv("spotify_data_with_genres.csv")
health_data = pd.read_csv("HKQuantityTypeIdentifierHeadphoneAudioExposure_filtered.csv")

# Preprocess Spotify data
spotify_data['ts'] = pd.to_datetime(spotify_data['ts'])
spotify_data['date'] = spotify_data['ts'].dt.date

# Calculate listening time in minutes
spotify_data['listening_time_minutes'] = spotify_data['ms_played'] / 60000

daily_listening = spotify_data.groupby('date')['listening_time_minutes'].sum().reset_index()
daily_listening.rename(columns={'listening_time_minutes': 'total_listening_time'}, inplace=True)

# Preprocess health data
health_data['startDate'] = pd.to_datetime(health_data['startDate'])
health_data['date'] = health_data['startDate'].dt.date

# Combine calories burned and steps data
combined_data = health_data.groupby('date')[['value']].mean().reset_index()
combined_data.rename(columns={'value': 'calories_burned_per_minute'}, inplace=True)

# Merge Spotify and health data
merged_data = pd.merge(daily_listening, combined_data, on='date', how='inner')

# Remove rows with missing or invalid data
merged_data.dropna(inplace=True)

# Descriptive Statistics
print("Descriptive Statistics for Listening Time and Calories Burned Per Minute:")
print(merged_data.describe())

# Pearson Correlation Test
corr, p_value = pearsonr(merged_data['total_listening_time'], merged_data['calories_burned_per_minute'])
print("\nPearson Correlation Test Results:")
print(f"Correlation Coefficient: {corr}")
print(f"P-value: {p_value}")

# Scatter Plot
plt.figure(figsize=(8, 6))
plt.scatter(merged_data['total_listening_time'], merged_data['calories_burned_per_minute'], alpha=0.6, color='blue')
plt.title("Scatter Plot of Listening Time vs Calories Burned Per Minute")
plt.xlabel("Total Listening Time (minutes)")
plt.ylabel("Calories Burned Per Minute")
plt.grid(True)
plt.show()

# Linear Regression
X = merged_data['total_listening_time']
X = sm.add_constant(X)  # Add constant for intercept
y = merged_data['calories_burned_per_minute']

model = sm.OLS(y, X).fit()
print("\nOLS Regression Results:")
print(model.summary())
