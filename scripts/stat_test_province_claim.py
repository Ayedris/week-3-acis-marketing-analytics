import pandas as pd
from scipy.stats import chi2_contingency
from pathlib import Path

# Load data
file_path = Path("C:/Users/ayedr/week-3-acis-marketing-analytics/processed/cleaned_train_set.csv")
df = pd.read_csv(file_path, low_memory=False)

# Drop missing values in relevant columns
df = df.dropna(subset=['Province', 'TotalClaims'])

# Create Claim Frequency column (KPI)
df['Claim_Frequency'] = df['TotalClaims'].apply(lambda x: 1 if x > 0 else 0)

# Build contingency table
contingency_table = pd.crosstab(df['Province'], df['Claim_Frequency'])

# Perform Chi-squared test
chi2, p, dof, expected = chi2_contingency(contingency_table)

# Output results
print("Chi-squared Test: Province vs Claim Frequency")
print("------------------------------------------------")
print("Contingency Table:\n", contingency_table)
print("\nExpected Frequencies:\n", pd.DataFrame(expected, index=contingency_table.index, columns=contingency_table.columns))
print(f"\nChi-squared statistic = {chi2:.4f}")
print(f"Degrees of Freedom = {dof}")
print(f"P-value = {p:.4f}")

# Interpretation
if p < 0.05:
    print("✅ Reject the null hypothesis: Significant risk differences across provinces.")
else:
    print("❌ Fail to reject the null hypothesis: No significant risk differences across provinces.")
