import pandas as pd
from scipy.stats import chi2_contingency, ttest_ind
from pathlib import Path

# Load the dataset
file_path = Path("C:/Users/ayedr/week-3-acis-marketing-analytics/processed/cleaned_train_set.csv")
df = pd.read_csv(file_path, low_memory=False)

# Prepare KPI: Claim Frequency
df['Claim_Frequency'] = df['TotalClaims'].apply(lambda x: 1 if x > 0 else 0)

# ---- Hypothesis 2: Risk Differences Between Zip Codes ----
print("\nChi-squared Test: PostalCode vs Claim Frequency")
df_zip = df.dropna(subset=['PostalCode', 'Claim_Frequency'])
contingency_zip = pd.crosstab(df_zip['PostalCode'], df_zip['Claim_Frequency'])
chi2_zip, p_zip, dof_zip, expected_zip = chi2_contingency(contingency_zip)

print(f"Chi2 Statistic: {chi2_zip:.4f}")
print(f"P-value: {p_zip:.4f}")
if p_zip < 0.05:
    print("✅ Reject H₀: Significant risk differences between zip codes.")
else:
    print("❌ Fail to reject H₀: No significant risk difference across zip codes.")

# ---- Hypothesis 3: Profit Margin Difference Between Zip Codes ----
print("\nT-test: Profit Margin between two largest Zip Codes")
df_margin = df.dropna(subset=['PostalCode', 'TotalPremium', 'TotalClaims'])
df_margin['ProfitMargin'] = df_margin['TotalPremium'] - df_margin['TotalClaims']

# Choose top 2 most common postal codes
top_zips = df_margin['PostalCode'].value_counts().nlargest(2).index.tolist()
group_a = df_margin[df_margin['PostalCode'] == top_zips[0]]['ProfitMargin']
group_b = df_margin[df_margin['PostalCode'] == top_zips[1]]['ProfitMargin']

t_stat, p_val = ttest_ind(group_a, group_b, equal_var=False)

print(f"Zip A: {top_zips[0]} vs Zip B: {top_zips[1]}")
print(f"T-statistic: {t_stat:.4f}")
print(f"P-value: {p_val:.4f}")
if p_val < 0.05:
    print("✅ Reject H₀: Profit margin differs significantly between these zip codes.")
else:
    print("❌ Fail to reject H₀: No significant margin difference between these zip codes.")
