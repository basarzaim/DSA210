import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
audio_exposure_data = pd.read_csv('HKQuantityTypeIdentifierHeadphoneAudioExposure_filtered.csv')
calories_burned_data = pd.read_csv('HKQuantityTypeIdentifierActiveEnergyBurned_filtered.csv')
steps_data = pd.read_csv('HKQuantityTypeIdentifierDistanceWalkingRunning_filtered.csv')

# Preprocess the data
audio_exposure_data['startDate'] = pd.to_datetime(audio_exposure_data['startDate'])
calories_burned_data['startDate'] = pd.to_datetime(calories_burned_data['startDate'])
steps_data['startDate'] = pd.to_datetime(steps_data['startDate'])

# Aggregate audio exposure data by daily average
audio_exposure_daily = (
    audio_exposure_data.groupby(audio_exposure_data['startDate'].dt.date)['value']
    .mean()
    .reset_index()
    .rename(columns={'startDate': 'Date', 'value': 'Avg_Audio_Exposure_dB'})
)

# Aggregate calories burned data by daily sum
calories_daily = (
    calories_burned_data.groupby(calories_burned_data['startDate'].dt.date)['value']
    .sum()
    .reset_index()
    .rename(columns={'startDate': 'Date', 'value': 'Total_Calories_Burned'})
)

# Aggregate steps data by daily sum
steps_daily = (
    steps_data.groupby(steps_data['startDate'].dt.date)['value']
    .sum()
    .reset_index()
    .rename(columns={'startDate': 'Date', 'value': 'Total_Steps'})
)

# Merge the datasets
merged_data = (
    audio_exposure_daily
    .merge(calories_daily, on='Date', how='inner')
    .merge(steps_daily, on='Date', how='inner')
)

# Scatter Plot: Audio Exposure vs Calories Burned
plt.figure(figsize=(10, 6))
sns.regplot(
    x='Avg_Audio_Exposure_dB',
    y='Total_Calories_Burned',
    data=merged_data,
    color='red',
    line_kws={"linewidth": 2}
)
plt.title('Audio Exposure vs Calories Burned')
plt.xlabel('Average Audio Exposure (dB)')
plt.ylabel('Total Calories Burned')
plt.tight_layout()
plt.show()

# Scatter Plot: Audio Exposure vs Steps
plt.figure(figsize=(10, 6))
sns.regplot(
    x='Avg_Audio_Exposure_dB',
    y='Total_Steps',
    data=merged_data,
    color='blue',
    line_kws={"linewidth": 2}
)
plt.title('Audio Exposure vs Steps')
plt.xlabel('Average Audio Exposure (dB)')
plt.ylabel('Total Steps')
plt.tight_layout()
plt.show()
