import pandas as pd
import numpy as np

# Load the data
file_path = 'C:\\Users\\ayedr\\week-3\\Data\\MachineLearningRating_v3.txt'
df = pd.read_csv(file_path, delimiter='|', low_memory=False)

# Fix dtype issues
df['CapitalOutstanding'] = pd.to_numeric(df['CapitalOutstanding'], errors='coerce')
df['CrossBorder'] = df['CrossBorder'].astype(str)

# Drop columns that are 100% missing
df = df.dropna(axis=1, how='all')

# Convert TransactionMonth to datetime
df['TransactionMonth'] = pd.to_datetime(df['TransactionMonth'], errors='coerce')

# Extract year and month for trend analysis
df['TransactionYear'] = df['TransactionMonth'].dt.year
df['TransactionMonthNum'] = df['TransactionMonth'].dt.month

# Optional: check skewed columns and log transform those that are highly skewed
numeric_cols = df.select_dtypes(include=[np.number]).columns
skewed = df[numeric_cols].skew().sort_values(ascending=False)

# Print skewness values (top 10)
print("\n📈 Skewed Columns (Top 10):")
print(skewed.head(10))

# Example: log-transform skewed columns (you can choose threshold e.g., >2)
for col in skewed.index:
    if abs(skewed[col]) > 2 and (df[col] > 0).all():
        df[f'{col}_log'] = np.log1p(df[col])

# Save cleaned version
df.to_csv('C://Users//ayedr//week-3//Data//processed//cleaned_train_set.csv', index=False)
print("\n✅ Cleaned data saved to 'C:/Users/ayedr/week-3/Data/cleaned_train_set.csv'")
