1. Project Overview

This project analyzes a Social Media & Mental Health dataset to explore relationships between social media usage and mental health indicators such as anxiety, depression, and sleep behavior.

The focus is on data-driven decision-making, including:

    Data cleaning and preparation strategies

    Assumptions and trade-offs

    Insightful visualizations

    Interpretation of patterns

2. Objectives

    Clean and prepare raw behavioral data for analysis

    Identify patterns linking social media usage to mental health

    Use visualizations to answer analytical questions

    Document reasoning behind each transformation

3. Technologies Used

    Python 3

    Pandas – Data manipulation

    NumPy – Numerical operations

    Matplotlib & Seaborn – Data visualization

4. Dataset

    Contains anonymized user data including:

        Age

        Daily screen time

        Sleep duration

        Anxiety score (GAD-7)

        Depression score (PHQ-9)

        Primary social media platform

        Mental health severity categories

5. Data Cleaning & Preparation

    Key steps include:

        Missing Values – Removed rows with missing critical data to improve reliability.

        Duplicates – Removed repeated records to avoid biased results.

        Data Types – Converted numeric columns stored as text.

        Outliers – Removed unrealistic screen time (>16 hours/day) and sleep duration (<2 or >12 hours).

        Feature Engineering – Created Screen_Time_Category (Low, Moderate, High, Very High) for interpretability.

6. Data Visualization

    Designed to answer specific questions:

        Screen Time Distribution (Histogram) – Understand usage behavior

        Screen Time vs Anxiety (Scatter Plot) – Explore numeric relationships

        Sleep Duration by Screen Time (Box Plot) – Compare sleep across usage levels

        Anxiety Severity by Platform (Count Plot) – Compare mental health across platforms

7. Expected Insights

    Skewed distribution toward heavy social media usage

    Mild positive relationship between screen time and anxiety

    Reduced sleep among heavy users

    Variation in mental health severity across platforms

8. Assumptions & Limitations

    Assumptions:

        Data entries are truthful and independent

        Missing values occur randomly

        Behavioral thresholds are realistic

    Limitations:

        Correlation does not imply causation

        Self-reported data may contain bias

        External lifestyle factors are not included

9. How to Run
    # Install dependencies
    pip install pandas numpy matplotlib seaborn

    # Run analysis
    python analysis.py

10. Project Structure
    project/
    │
    ├── social_media_mental_health.csv
    ├── analysis.py
    └── README.md