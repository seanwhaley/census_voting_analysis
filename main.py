import pandas as pd
import os

# Step 1: Import Necessary Libraries
# Libraries have been imported above

# Step 2: Load Census Data from Local File
def get_census_data():
    df_census = pd.read_csv('data/census_data.csv')
    return df_census

# Step 3: Load Voting Data from Local File
def get_voting_data():
    df_voting = pd.read_csv('data/voting_data.csv')
    return df_voting

# Step 4: Data Cleaning
def clean_data(df_census, df_voting):
    # Convert geographic identifiers to a common format
    df_census['GEOID'] = df_census['ST'].astype(str).str.zfill(2) + df_census['PUMA'].astype(str).str.zfill(5)  # Adjust as needed
    df_voting['GEOID'] = df_voting['county_fips'].astype(str).str.zfill(5) + df_voting['precinct'].astype(str).str.zfill(5)  # Adjust as needed
    return df_census, df_voting

# Step 5: Merge Datasets
def merge_data(df_census, df_voting):
    df_merged = pd.merge(df_census, df_voting, on='GEOID')
    return df_merged

# Step 6: Analyze Data
def analyze_data(df_merged):
    correlation_matrix = df_merged.corr()
    return correlation_matrix

# Step 7: Visualize Data
def visualize_data(df_merged):
    import matplotlib.pyplot as plt
    import seaborn as sns
    sns.heatmap(df_merged.corr(), annot=True, cmap="coolwarm")
    plt.show()

# Example usage
df_census = get_census_data()
df_voting = get_voting_data()
df_census, df_voting = clean_data(df_census, df_voting)
df_merged = merge_data(df_census, df_voting)
correlation_matrix = analyze_data(df_merged)
visualize_data(df_merged)
