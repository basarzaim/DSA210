# DSA210: Spotify and Health Data Analysis

This repository contains a data science project analyzing the correlation between music listening habits and health metrics. It uses personal data from Spotify and wearable devices to explore how music genres, listening durations, and patterns relate to physical activity and overall health.

## **Motivation**

Music is a significant part of daily life, and its influence on physical activity is often discussed but rarely quantified. This project aims to uncover insights about how music genres, listening durations, and patterns affect various health metrics like calorie burn, steps, and heart rate. By analyzing personal Spotify and health data, this project seeks to establish meaningful correlations and explore trends that might inform personalized fitness or wellness strategies.

## **Research Questions**
1. How do different music genres influence physical activity (e.g., calories burned, steps)?
2. Is there a correlation between listening time and exercise intensity?
3. Are specific genres associated with higher or lower physical activity levels?
4. Does headphone audio exposure correlate with changes in physical activity or calorie burn levels?
5. Does listening to certain genres for prolonged periods affect walking speed or asymmetry metrics?
6. Is there a relationship between music genres and headphone audio exposure levels?

## **Data**
- **Health Data**: Collected from wearable device and mobile phone between 2021-2024. Metrics include calories burned, step count , average headphone exposure etc. Data for 2021-2023 has been filtered out, aligning the analysis with 2024 Spotify data.
- **Spotify Data**: Listening history from Spotify's API, including genres, track names, and listening durations for 2024.
- **Data:** Filtered health and Spotify data (*.csv files) from 2024-02-16 to 2024-11-25. [View data in csv format](./Filtered_data)
- **Graphs:** Visualizations of weekly trends for each dataset, saved as images in the Outputs folder. [View data on graphs](./Filtered_data/Outputs_Graph)
- **Graph Generation Code:** The graph.py file contains the Python functions used to generate the graphs. [View the python code for deriving graphs.](./Filtered_data/graph_functions.py)

1. Clone the repository:
   ```bash
   git clone https://github.com/basarzaim/DSA210
   cd DSA210
