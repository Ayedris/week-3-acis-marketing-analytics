import pandas as pd
from scipy.stats import ttest_ind
from pathlib import Path

# Load the dataset
file_path = Path("C:/Users/ayedr/week-3-acis-marketing-analytics/processed/cleaned_train_set.csv")
df = pd.read_csv(file_path, low_memory=False)

# Calculate Profit Margin
df['ProfitMargin'] = df['TotalPremium'] - df['TotalClaims']

# Drop rows with missing postal code or profit margin
df = df.dropna(subset=['PostalCode', 'ProfitMargin'])

# Select top 2 ZIP codes with the most data
top_zips = df['PostalCode'].value_counts().nlargest(2).index.tolist()

# Group A and B
group_a = df[df['PostalCode'] == top_zips[0]]['ProfitMargin']
group_b = df[df['PostalCode'] == top_zips[1]]['ProfitMargin']

# Welch’s t-test
t_stat, p_val = ttest_ind(group_a, group_b, equal_var=False)

# Print results
print(f"T-test: Profit Margin between ZIP {top_zips[0]} and ZIP {top_zips[1]}")
print(f"T-statistic: {t_stat:.4f}")
print(f"P-value: {p_val:.4f}")

if p_val < 0.05:
    print("✅ Reject the null hypothesis: Significant margin difference between ZIP codes.")
else:
    print("❌ Fail to reject the null hypothesis: No significant margin difference between ZIP codes.")
