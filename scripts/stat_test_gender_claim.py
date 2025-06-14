import pandas as pd
from scipy.stats import ttest_ind
from pathlib import Path

# Load cleaned data
file_path = Path("C:/Users/ayedr/week-3-acis-marketing-analytics/processed/cleaned_train_set.csv")
df = pd.read_csv(file_path, low_memory=False)


# Create Claim Frequency column
df['Claim_Frequency'] = df['TotalClaims'].apply(lambda x: 1 if x > 0 else 0)

# Drop NaNs in Gender and Claim_Frequency
df = df.dropna(subset=['Gender', 'Claim_Frequency'])

# Split groups
group_m = df[df['Gender'] == 'Male']['Claim_Frequency']
group_f = df[df['Gender'] == 'Female']['Claim_Frequency']

# t-test (equal_var=False for Welch’s t-test, which is safer if variances differ)
t_stat, p_value = ttest_ind(group_m, group_f, equal_var=False)

print("T-test Results: Gender vs Claim Frequency")
print(f"T-statistic: {t_stat:.4f}")
print(f"P-value: {p_value:.4f}")

# Interpretation
if p_value < 0.05:
    print("✅ Reject the null hypothesis: Significant difference in claim frequency between genders.")
else:
    print("❌ Fail to reject the null hypothesis: No significant difference between genders.")
