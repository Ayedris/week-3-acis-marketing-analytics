import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Load cleaned data
file_path = Path("C:/Users/ayedr/week-3-acis-marketing-analytics/processed/cleaned_train_set.csv")
df = pd.read_csv(file_path, low_memory=False)

# Clean column names
df.columns = df.columns.str.strip()

"""
top_zip = df.groupby("PostalCode")[["TotalPremium", "TotalClaims"]].sum().nlargest(10, 'TotalPremium')

# Plot heatmap
sns.heatmap(top_zip, annot=True, cmap="YlGnBu")
plt.title("Top 10 Postal Codes by Premium and Claim Totals")
plt.tight_layout()
plt.show()

#Bar Plot: Distribution of Insurance Cover Type Across Citizenship

# Clean column names (in case there are extra spaces)
df.columns = df.columns.str.strip()

top_cover_types = df['CoverType'].value_counts().nlargest(16).index
filtered_df = df[df['CoverType'].isin(top_cover_types)]

plt.figure(figsize=(12, 6))
sns.countplot(data=filtered_df, x="CoverType", hue="Citizenship", palette='tab20', alpha=0.6)
plt.title("Top Insurance Cover Types by Citizenship")
plt.xticks(rotation=30, ha='right', fontsize=9)
plt.tight_layout()
plt.show()

"""
#plot of Time Trend: Monthly Average Premium vs Claims 

# Convert TransactionMonth to datetime
df['TransactionMonth'] = pd.to_datetime(df['TransactionMonth'], errors='coerce')

# Drop rows with invalid dates (if any)
df = df.dropna(subset=['TransactionMonth'])

# Group by month and compute mean of Premium and Claims
monthly = df.groupby(df['TransactionMonth'].dt.to_period('M')).agg({
    'TotalPremium': 'mean',
    'TotalClaims': 'mean'
}).reset_index()

# Convert Period to string for plotting
monthly['TransactionMonth'] = monthly['TransactionMonth'].astype(str)

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(monthly['TransactionMonth'], monthly['TotalPremium'], label='Avg Premium', marker='o')
plt.plot(monthly['TransactionMonth'], monthly['TotalClaims'], label='Avg Claims', marker='x')
plt.title("Monthly Trends: Average Premium vs Average Claims")
plt.xlabel("Month")
plt.ylabel("Amount (ZAR)")
plt.xticks(rotation=45)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
