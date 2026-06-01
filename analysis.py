import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data.csv")

# Show first 5 rows
print("First 5 rows:")
print(df.head())

# Basic info
print("\nDataset Info:")
print(df.info())

# If math score column exists
if 'math score' in df.columns:
    print("\nAverage Math Score:")
    print(df['math score'].mean())

# GroupBy example
if 'gender' in df.columns and 'math score' in df.columns:
    print("\nAverage Math Score by Gender:")
    print(df.groupby('gender')['math score'].mean())

    df.groupby('gender')['math score'].mean().plot(kind='bar')
    plt.title("Average Math Score by Gender")
    plt.ylabel("Average Score")
    plt.show()
