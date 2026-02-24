"""
Project: Social Media & Mental Health Analysis
Language: Python 3
Libraries: pandas, numpy, matplotlib, seaborn

GOAL:
-----
1. Clean and prepare the dataset
2. Explain WHY each cleaning decision is made
3. Perform intentional visualizations
4. Extract meaningful insights from visuals

NOTE:
-----
This script emphasizes decision-making and analytical reasoning,
not just code execution.
"""

# ============================================================
# 1. IMPORT LIBRARIES
# ============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Visualization style for readability
sns.set_theme()

# ------------------------------------------------------------
# WHY THESE LIBRARIES?
# pandas   -> data manipulation
# numpy    -> numerical handling
# matplotlib/seaborn -> visualization & pattern discovery
# ------------------------------------------------------------


# ============================================================
# 2. LOAD DATA
# ============================================================

# Load dataset
df = pd.read_csv("social_media_mental_health.csv")

# Quick inspection
print("Dataset Shape:", df.shape)
print("\nColumns:\n", df.columns)
print("\nSample Data:\n", df.head())


# ============================================================
# 3. DATA CLEANING & PREPARATION
# ============================================================

"""
This section focuses on analytical decision-making.

Questions addressed:
- What cleaning steps were performed?
- Why were they necessary?
- What assumptions were made?
- What trade-offs were considered?
"""


# ------------------------------------------------------------
# STEP 1: CHECK MISSING VALUES
# ------------------------------------------------------------

print("\nMissing Values:\n", df.isnull().sum())

"""
DECISION:
---------
We check missing values first because:
- Missing behavioral or health scores could bias analysis.
- Visualization tools may fail or misrepresent trends.

ASSUMPTION:
-----------
If only a small percentage of values are missing,
removal is safer than imputation.

TRADE-OFF:
----------
Dropping rows reduces dataset size but prevents
introducing artificial patterns via guessing values.
"""


# Drop rows with missing values (if any exist)
df = df.dropna()



# ------------------------------------------------------------
# STEP 2: REMOVE DUPLICATES
# ------------------------------------------------------------

duplicates = df.duplicated().sum()
print("Duplicate Rows:", duplicates)

"""
WHY?
----
Duplicate users can skew averages and correlations,
especially behavioral metrics like screen time.

ASSUMPTION:
-----------
Each User_ID should represent one unique individual.

TRADE-OFF:
----------
Removing duplicates may discard repeated observations,
but improves statistical integrity.
"""

df = df.drop_duplicates()



# ------------------------------------------------------------
# STEP 3: DATA TYPE VALIDATION
# ------------------------------------------------------------

print("\nData Types:\n", df.dtypes)

"""
WHY?
----
Incorrect data types can break aggregations and visualizations.
Example:
- Numeric values stored as strings cannot be averaged.
"""

# Ensure numeric columns are numeric
numeric_cols = [
    "Age",
    "Daily_Screen_Time_Hours",
    "Sleep_Duration_Hours",
    "GAD_7_Score",
    "PHQ_9_Score"
]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")


# ------------------------------------------------------------
# STEP 4: HANDLE OUTLIERS
# ------------------------------------------------------------

"""
WHY OUTLIERS MATTER:
-------------------
Extreme values (e.g., 24+ hours screen time)
may represent entry errors rather than reality.

ASSUMPTION:
-----------
Realistic daily screen time should be <= 16 hours.
Sleep duration should typically be between 2–12 hours.

TRADE-OFF:
----------
Removing extreme cases improves model reliability
but may remove rare real behaviors.
"""

df = df[
    (df["Daily_Screen_Time_Hours"] <= 16) &
    (df["Sleep_Duration_Hours"].between(2, 12))
]


# ------------------------------------------------------------
# STEP 5: FEATURE ENGINEERING
# ------------------------------------------------------------

"""
WHY CREATE NEW FEATURES?
------------------------
Derived features often reveal clearer patterns than raw values.

We create:
Screen_Time_Category → easier comparison groups
"""

df["Screen_Time_Category"] = pd.cut(
    df["Daily_Screen_Time_Hours"],
    bins=[0, 2, 5, 8, 16],
    labels=["Low", "Moderate", "High", "Very High"]
)

"""
ASSUMPTION:
-----------
Behavioral impact changes at meaningful usage thresholds.

TRADE-OFF:
----------
Binning simplifies analysis but loses numeric precision.
"""



# ============================================================
# 4. DATA UNDERSTANDING & VISUALIZATION
# ============================================================

"""
Visualizations are intentional — not decorative.

Each visualization answers a specific question.
"""


# ------------------------------------------------------------
# Visualization 1: Screen Time Distribution
# ------------------------------------------------------------

plt.figure()
sns.histplot(df["Daily_Screen_Time_Hours"], bins=30)

plt.title("Distribution of Daily Screen Time")

"""
WHY THIS VISUAL?
----------------
Histogram shows overall behavioral distribution.

QUESTION ANSWERED:
Are most users moderate or heavy social media users?

INSIGHT TO LOOK FOR:
- Skew toward high usage?
- Multiple behavioral clusters?
"""

plt.show()



# ------------------------------------------------------------
# Visualization 2: Screen Time vs Anxiety (GAD-7)
# ------------------------------------------------------------

plt.figure()
sns.scatterplot(
    x="Daily_Screen_Time_Hours",
    y="GAD_7_Score",
    data=df
)

plt.title("Screen Time vs Anxiety Score")

"""
WHY SCATTER PLOT?
-----------------
Best visualization for relationship between two numeric variables.

QUESTION:
Does higher screen time correlate with anxiety?

PATTERNS TO OBSERVE:
- Upward trend → possible positive correlation
- Random scatter → weak relationship
"""

plt.show()



# ------------------------------------------------------------
# Visualization 3: Sleep Duration by Screen Time Category
# ------------------------------------------------------------

plt.figure()
sns.boxplot(
    x="Screen_Time_Category",
    y="Sleep_Duration_Hours",
    data=df
)

plt.title("Sleep Duration Across Screen Time Levels")

"""
WHY BOX PLOT?
-------------
Shows distribution, median, and variability.

QUESTION:
Do heavy social media users sleep less?

INSIGHT:
Lower median sleep in high-usage groups suggests
behavioral impact.
"""

plt.show()



# ------------------------------------------------------------
# Visualization 4: Mental Health Severity by Platform
# ------------------------------------------------------------

plt.figure(figsize=(10, 5))
sns.countplot(
    x="Primary_Platform",
    hue="GAD_7_Severity",
    data=df
)

plt.xticks(rotation=45)
plt.title("Anxiety Severity Across Platforms")

"""
WHY COUNT PLOT?
---------------
Categorical comparison visualization.

QUESTION:
Are certain platforms associated with higher anxiety levels?

VALUE:
Helps identify platform-specific behavioral trends.
"""

plt.show()



# ============================================================
# 5. SUMMARY OF FINDINGS (INTERPRETATION)
# ============================================================

"""
Typical Patterns You May Observe:
---------------------------------
1. Screen time distribution may be right-skewed
   → many high-usage users.

2. Scatterplot may show mild positive relationship
   between screen time and anxiety.

3. Boxplots often reveal reduced sleep in heavy users.

4. Platform comparison may show uneven mental health
   severity distributions.

HOW VISUALS ANSWER QUESTIONS:
-----------------------------
They transform abstract numeric relationships into
observable behavioral patterns, supporting evidence-based
conclusions rather than assumptions.
"""

print("\nAnalysis Complete.")