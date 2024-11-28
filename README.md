# DSA210
# Spotify and Health Data Analysis

## **Motivation**
This project explores the relationship between music listening habits and health metrics such as calorie burn, activity levels, and heart rate. By analyzing personal data, I aim to uncover insights about how music genres and listening patterns correlate with physical activities.

## **Research Questions**
1. How do different music genres influence physical activity (e.g., calories burned, steps)?
2. Is there a correlation between listening time and exercise intensity?
3. Are specific genres associated with higher or lower physical activity levels?

## **Data**
- **Health Data**: Collected from a wearable device (e.g., Fitbit) between 2021-2024. Metrics include calories burned, steps, and heart rate.
- **Spotify Data**: Listening history from Spotify's API, including genres, track names, and listening durations for 2024.

### **Data Cleaning**
- Filtered health data to align with 2024 Spotify data.
- Enriched Spotify data with genres fetched from Spotify's Web API.

## **Methods**
1. **Data Preprocessing**:
   - Merged Spotify and health datasets by timestamp.
   - Filtered data for valid matches within a specific timeframe.
2. **Exploratory Data Analysis (EDA)**:
   - Visualization of genre distributions and health metrics.
   - Temporal analysis (e.g., activity during different times of the day or week).
3. **Machine Learning**:
   - Regression models to predict calorie burn from listening habits.
   - Clustering to identify patterns in music-activity relationships.

## **Findings**
- [Placeholder for findings once analysis is complete.]

## **Limitations**
- Limited to 2024 Spotify data.
- Genre data may include multiple genres per track, requiring aggregation.
- Potential bias due to incomplete health tracking on some days.

## **Future Work**
- Expand analysis with additional years of Spotify data.
- Use more advanced models for predictive analysis.
- Explore mood and tempo data for a more nuanced relationship.

## **How to Run the Code**
1. Clone the repository:
   ```bash
   git clone https://github.com/basarzaim/DSA210
