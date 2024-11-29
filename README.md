# DSA210: Spotify and Health Data Analysis

This repository contains a data science project analyzing the correlation between music listening habits and health metrics. It uses personal data from Spotify and wearable devices to explore how music genres, listening durations, and patterns relate to physical activity and overall health.

## **Motivation**

Music is a significant part of daily life, and its influence on physical activity is often discussed but rarely quantified. This project aims to uncover insights about how music genres, listening durations, and patterns affect various health metrics like calorie burn, steps, and heart rate. By analyzing personal Spotify and health data, this project seeks to establish meaningful correlations and explore trends that might inform personalized fitness or wellness strategies.

## **Research Questions**
1. How do different music genres influence physical activity (e.g., calories burned, steps)?
2. Is there a correlation between listening time and exercise intensity?
3. Are specific genres associated with higher or lower physical activity levels?

## **Data**
- **Health Data**: Collected from wearable device and mobile phone between 2021-2024. Metrics include calories burned, step count , average headphone exposure etc. Data for 2021-2023 has been filtered out, aligning the analysis with 2024 Spotify data.
- **Spotify Data**: Listening history from Spotify's API, including genres, track names, and listening durations for 2024.

## **Methodology**
1. **Data Cleaning**:
   - Filtered health data to align with Spotify data for 2024.
   - Enriched Spotify data with genres fetched from Spotify's Web API.
2. **Exploratory Data Analysis (EDA)**:
   - Visualized weekly trends for each health metric.
   - Analyzed Spotify listening time and genre distributions over time.
3. **Modeling**:
   - Built regression models to predict calorie burn based on listening habits.
   - Used clustering to identify patterns between genres and physical activity.

## **Findings**
-----------------------

## **Limitations**
- Limited to 2024 Spotify data.
- Genre data may include multiple genres per track, requiring aggregation.
- Potential bias due to incomplete health tracking on some days.


## **How to Run the Code**

1. Clone the repository:
   ```bash
   git clone https://github.com/basarzaim/DSA210
   cd DSA210
