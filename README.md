# **DSA210: Spotify and Health Data Analysis**

This repository contains a data science project analyzing the correlation between music listening habits and health metrics. It uses personal data from Spotify and health metrics from a wearable device and mobile phone to explore how music genres, listening durations, and patterns relate to physical activity and overall health.

[This is the final report of the project.](https://basarzaimdsa.netlify.app/)

---

## **Table of Contents**
- [Motivation](#motivation)
- [Research Questions](#research-questions)
- [Data](#data)
- [Methodology](#methodology)
- [Findings](#findings)
- [Limitations](#limitations)
- [Future Directions](#future-directions)
- [Repository Structure](#repository-structure)

---

## **Motivation**

Music is a significant part of daily life, and its influence on physical activity is often discussed but rarely quantified. This project aims to uncover insights into how music genres, listening durations, and patterns affect various health metrics like calorie burn, steps, and heart rate. By analyzing personal Spotify and health data, this project seeks to establish meaningful correlations and explore trends that might inform personalized fitness or wellness strategies.

---

## **Research Questions**

1. How do different music genres influence physical activity (e.g., calories burned, steps)?
2. Is there a correlation between listening time and exercise intensity?
3. Are specific genres associated with higher or lower physical activity levels?
4. Does headphone audio exposure correlate with changes in physical activity or calorie burn levels?
5. Is there a relationship between prolonged listening to specific music genres and changes in walking speed or asymmetry metrics?
6. Is there a relationship between music genres and headphone audio exposure levels?

---

## **Data**

### **1. Health Data**
- Collected from Apple Health between 2021-2024.
- Metrics include:
  - Calories burned
  - Step count
  - Walking speed
  - Walking asymmetry
  - Average headphone exposure levels
- Impractical data were extracted.
- Data from 2021-2023 was excluded to align with Spotify data from 2024.

### **2. Spotify Data**
- Listening history exported using the Spotify API for 2024.
- An API key was used to extract genres for tracks. Subgenres were mapped into broader genres for ease of analysis.

### **3. Final Data**
- Filtered health and Spotify data (*.csv files) covering February to November 2024.

---

## **Methodology**

### **1. Data Collection**
- Health metrics were exported from Apple Health.
- Spotify listening data was requested, genre informations were extracted via API requests.
- Genres were mapped into broader categories (e.g., "german metal" → "Metal"):
  ```python
  genre_mapping = {
      'german metal': 'Metal',
      'hard rock': 'Rock',
      'dance pop': 'Pop',
      ...
  }
  ```

### **2. Data Preprocessing**
- Filtered data to align both sources within the same date range.
- Merged genres into broader categories.
- Removed incomplete or irrelevant metrics, such as "walking double support percentage."

### **3. Exploratory Data Analysis (EDA)**
EDA techniques were used to:
- Understand distributions of health metrics and listening durations.
- Identify patterns and anomalies.
- Create visualizations such as scatter plots, bar charts, and boxplots to explore potential relationships.

### **4. Analysis**
Addressed each research question using:
- Descriptive Statistics: Explored central tendencies, variability, and distributions in the data for different genres, listening durations, and activity metrics.
- Statistical tests
  - Chi Square Test: Used in Question 1 to analyze relationships between music genres and activity levels.
  - Pearson Correlation and OLS Regression: Applied in Question 2 to measure the correlation between listening time and exercise intensity.
  - ANOVA Test: Used in Questions 5 and 6 to compare group means (e.g., prolonged listening and walking speed).
- Visualizations: Utilized a variety of visual tools to uncover patterns and relationships:
---

## **Findings**
Check the [report](https://basarzaimdsa.netlify.app/) for the detailed findings.

### **1. Music Genres vs Physical Activity**
-Energetic genres (e.g., Metal, Rock, and Electronic) showed minor associations with higher activity levels. No strong correlation was observed between genres and physical activity metrics.

### **2. Listening Time vs Exercise Intensity**
-Scatter plots revealed no significant correlation between listening time and exercise intensity metrics like steps or calories burned per minute.

### **3. Genre-Specific Walking Metrics**
-Prolonged listening to specific genres did not significantly impact walking speed or asymmetry.

### **4. Headphone Audio Exposure**
-Average headphone audio exposure levels were similar across genres, with no strong genre-specific trends.

---

## **Limitations**

### **1. Data Completeness**
- The scope of Apple Health metrics and Spotify listening data was limited.

### **2. Granularity**
- Aggregating data at daily/monthly levels may have masked finer patterns.

### **3. Causality**
- Observational data; correlations do not imply causation.

---

## **Future Directions**

### **1. Refinement**
- Include additional metrics such as workout types and sleep quality.

### **2. Personalization**
- Conduct user-specific analyses for tailored fitness insights.

### **3. Machine Learning**
- Use advanced models to predict activity levels based on music patterns.

---

## **Repository Structure**

- **Filtered_data/**:
  - Processed health and Spotify data in CSV format.
- **Outputs_Graph/**:
  - Contains visualizations for each research question.
- **graph_functions.py**:
  - Python codes for graph generations & analyses.
- **Report.pdf**:
  - Summary of research questions and findings.

---

## **Acknowledgments**

Special thanks to the tools and libraries used:
- Pandas, Matplotlib, and Seaborn for data analysis and visualization.
- Spotify API and Apple Health for data collection.
