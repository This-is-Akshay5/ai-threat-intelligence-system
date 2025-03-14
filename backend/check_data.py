import pandas as pd

# Load dataset
df = pd.read_csv("phishing_data.csv")

# Display dataset information
print("First 5 Rows of Dataset:")
print(df.head())  # Print the first 5 rows

print("\nColumn Names in Dataset:")
print(df.columns)  # Print all column names

print(f"\nTotal columns: {len(df.columns)}")  # Print total column count
