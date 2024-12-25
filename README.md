# DSA210: Spotify and Health Data Analysis

This repository contains a data science project analyzing the correlation between music listening habits and health metrics. It uses personal data from Spotify and health metrics from a wearable device and mobile phone to explore how music genres, listening durations, and patterns relate to physical activity and overall health.

## **Motivation**

Music is a significant part of daily life, and its influence on physical activity is often discussed but rarely quantified. This project aims to uncover insights about how music genres, listening durations, and patterns affect various health metrics like calorie burn, steps, and heart rate. By analyzing personal Spotify and health data, this project seeks to establish meaningful correlations and explore trends that might inform personalized fitness or wellness strategies.

## **Research Questions**
1. How do different music genres influence physical activity (e.g., calories burned, steps)?
2. Is there a correlation between listening time and exercise intensity?
3. Are specific genres associated with higher or lower physical activity levels?
4. Does headphone audio exposure correlate with changes in physical activity or calorie burn levels?
5. Is there a relationship between prolonged listening to specific music genres and changes in walking speed or asymmetry metrics?
6. Is there a relationship between music genres and headphone audio exposure levels?

## **Data**
- **Health Data**: Collected from wearable device and mobile phone between 2021-2024. Metrics include calories burned, step count , average headphone exposure etc. Data for 2021-2023 has been filtered out, aligning the analysis with 2024 Spotify data.
- **Spotify Data**: Listening history from Spotify's API, including genres, track names, and listening durations for 2024.
- **Data:** Filtered health and Spotify data (*.csv files) from 2024-02-16 to 2024-11-25. [View data in csv format](./Filtered_data)
- **Graphs:** Visualizations of weekly trends for each dataset, saved as images in the "Outputs_Graph" folder. [View data on graphs](./Filtered_data/Outputs_Graph)
- **Graph Generation Code:** The graph.py file contains the Python functions used to generate the graphs. [View the python code for deriving graphs.](./Filtered_data/graph_functions.py)

## **Methodology**
-- **Data Collection**: Health metrics were collected from wearable devices and mobile phones, while Spotify API provided listening history, including genres and durations.
-- **Preprocessing**: Data was filtered to include only 2024, genres were mapped to broader categories, and daily and monthly aggregates were calculated.
-- **Analysis**: Each research question was addressed using appropriate visualizations (e.g., bar charts, scatter plots, and boxplots) and statistical correlation tests.
-- **Visualization**: Trends and distributions were explored to identify relationships between music habits and health metrics like calories burned, steps, and walking asymmetry.
-- **Reporting**: Observations, conclusions, and limitations were documented for each question.

## **Findings**
**1. Music Genres vs Physical Activity:**
- Energetic genres (e.g., Metal, Rock, and Electronic) showed minor associations with higher activity levels.
- No strong correlation was observed between music genres and physical activity metrics.

**2. Listening Time vs Exercise Intensity:**
- No significant correlation was found between total listening time and exercise intensity (e.g., steps/calories burned).

**3. Genre-Specific Analysis of Walking Metrics:**
- Prolonged listening to specific genres did not significantly impact walking speed or asymmetry.

**4. Headphone Audio Exposure:**
-Average headphone audio exposure levels were similar across genres, with no genre-specific trends.


## **Limitations**
-Granularity:
-Aggregated data (daily/monthly) may have masked finer patterns.

-External Factors:
-Activity levels and audio exposure might be influenced by factors outside the dataset (e.g., lifestyle, environmental noise).

-Causality:
-Correlations do not imply causation due to the observational nature of the data.

## **Future Directions**
-Refinement:
-Include additional data, such as workout types and user demographics, for deeper analysis.
-Personalization:
-Analyze individual-level trends to uncover personalized insights.
-Long-Term Trends:
-Examine data over extended periods to identify seasonal patterns.

## **Repository Structure**
-**Filtered_data/:**
-Contains filtered health and Spotify data in CSV format.
-**Outputs_Graph/:**
-Stores visualizations for each research question.
-**graph_functions.py:**
-Python code for data preprocessing and visualization.
-**Report.pdf:**
-A comprehensive report summarizing findings, methodologies, and limitations.
