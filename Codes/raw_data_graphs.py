import pandas as pd
import matplotlib.pyplot as plt
import os

# Define the date range
start_date = "2024-02-16"
end_date = "2024-11-25"

# Load Spotify data
spotify_data = pd.read_csv(r"C:\Users\Basar\data\Filtered_data\spotify_data_with_genres.csv")
spotify_data["ts"] = pd.to_datetime(spotify_data["ts"]).dt.date

# Filter Spotify data by date
spotify_data = spotify_data[(spotify_data["ts"] >= pd.to_datetime(start_date).date()) & 
                             (spotify_data["ts"] <= pd.to_datetime(end_date).date())]

# Convert to weekly averages for Spotify listening time
spotify_data["week"] = pd.to_datetime(spotify_data["ts"]).dt.to_period("W")
spotify_weekly = spotify_data.groupby("week")["ms_played"].sum().reset_index()
spotify_weekly["ms_played"] = spotify_weekly["ms_played"] / (1000 * 60)  # Convert to minutes

plt.figure(figsize=(10, 6))
plt.plot(spotify_weekly["week"].astype(str), spotify_weekly["ms_played"], marker="o", linestyle="-", color="blue")
plt.title("Spotify Weekly Listening Time")
plt.xlabel("Week")
plt.ylabel("Listening Time (minutes)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(r"C:\Users\Basar\data\Filtered_data\Outputs\spotify_weekly_listening.png")
plt.show()

# Define a mapping of metrics to their units
metric_units = {
    "HKCategoryTypeIdentifierHeadphoneAudioExposureEvent_filtered": "dB",
    "HKQuantityTypeIdentifierStepCount_filtered": "Steps",
    "HKQuantityTypeIdentifierActiveEnergyBurned_filtered": "kcal",
    "HKQuantityTypeIdentifierBasalEnergyBurned_filtered": "kcal",
    "HKQuantityTypeIdentifierDistanceWalkingRunning_filtered": "km",
    "HKQuantityTypeIdentifierFlightsClimbed_filtered": "Flights",
    "HKQuantityTypeIdentifierHeadphoneAudioExposure_filtered": "dB",
    "HKQuantityTypeIdentifierWalkingAsymmetryPercentage_filtered": "%",
    "HKQuantityTypeIdentifierWalkingDoubleSupportPercentage_filtered": "%",
    "HKQuantityTypeIdentifierWalkingSpeed_filtered": "m/s",
    "HKQuantityTypeIdentifierWalkingStepLength_filtered": "cm",
}


# Aggregate health data by week
health_data_folder = r"C:\Users\Basar\data\Filtered_data"
health_dfs = {}
output_folder = r"C:\Users\Basar\data\Filtered_data\Outputs"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for file in os.listdir(health_data_folder):
    if file.endswith(".csv"):
        file_path = os.path.join(health_data_folder, file)
        try:
            df = pd.read_csv(file_path)
            print(f"Processing file: {file}")
            
            # Ensure 'startDate' and 'value' columns exist
            if "startDate" in df.columns and "value" in df.columns:
                df["startDate"] = pd.to_datetime(df["startDate"]).dt.date
                
                # Ensure 'value' column is numeric
                df["value"] = pd.to_numeric(df["value"], errors="coerce")
                df = df.dropna(subset=["value"])
                
                df["week"] = pd.to_datetime(df["startDate"]).dt.to_period("W")
                df = df[(df["startDate"] >= pd.to_datetime(start_date).date()) & 
                        (df["startDate"] <= pd.to_datetime(end_date).date())]
                
                # Group by week and calculate average
                weekly_data = df.groupby("week")["value"].mean().reset_index()
                health_dfs[file.split(".")[0]] = weekly_data

                # Plot the weekly data
                plt.figure(figsize=(10, 6))
                plt.plot(weekly_data["week"].astype(str), weekly_data["value"], marker="o", linestyle="-", label=file.split(".")[0])

                # Get the unit from the dictionary, default to an empty string if the metric isn't listed
                unit = metric_units.get(file.split(".")[0], "")

                plt.title(f"Weekly {file.split('.')[0]} Average")
                plt.xlabel("Week")
                plt.ylabel(f"Average Value ({unit})")  # Add the unit dynamically
                plt.xticks(rotation=45, fontsize=8)
                plt.legend()
                plt.tight_layout()
                plt.savefig(f"{output_folder}/{file.split('.')[0]}_weekly_trend.png")
                plt.show()
            else:
                print(f"Skipping {file}: Missing 'startDate' or 'value' column.")
        except Exception as e:
            print(f"Error processing file {file}: {e}")
