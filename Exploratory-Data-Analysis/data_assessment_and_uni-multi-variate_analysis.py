#data_assessment_and_uni-multi-variate_analysis.py
#Load Cleaned Data
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
# Load data
df = pd.read_csv('processed/cleaned_train_set.csv')

"""
#Descriptive Statistics
print(df[['TotalPremium', 'TotalClaims']].describe())

#Data Structure
print(df.dtypes)

#Data Quality Assessmen
missing_summary = df.isnull().sum()
print("Missing Values:\n", missing_summary[missing_summary > 0])

#Univariate Analysis
#Histograms for Numerical Variables
numeric_cols = df.select_dtypes(include='number').columns
df[numeric_cols].hist(figsize=(15, 12), bins=30)
plt.tight_layout()
plt.show()



#Bar Plots for Categorical Columns
categorical_cols = df.select_dtypes(include='object').columns
for col in categorical_cols[:5]:  
    plt.figure(figsize=(8, 4))
    sns.countplot(data=df, x=col, order=df[col].value_counts().index[:10])
    plt.xticks(rotation=45)
    plt.title(f'Distribution of {col}')
    plt.tight_layout()
    plt.show()


#Bivariate / Multivariate Analysis
#Correlation Matrix
corr_matrix = df[['TotalPremium', 'TotalClaims']].corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

"""
#Scatter Plot by ZipCode

plt.figure(figsize=(10, 8))
sns.scatterplot(data=df, x='TotalPremium', y='TotalClaims', hue='PostalCode', palette='tab20', alpha=0.6)
plt.title('TotalPremium vs TotalClaims by PostalCode')
plt.tight_layout()
plt.show()

df['PostalCodeBin'] = (df['PostalCode'] // 10) * 10

plt.figure(figsize=(10, 10))
sns.scatterplot(
    data=df,
    x='TotalPremium',
    y='TotalClaims',
    hue='PostalCodeBin',  # Use grouped bins
    palette='tab20',
    alpha=0.6
)
plt.title('TotalPremium vs TotalClaims (Grouped by PostalCode)')
plt.tight_layout()
plt.legend(title='PostalCode', bbox_to_anchor=(1, 1), loc='upper left')
plt.show()

#Outlier Detection with Box Plots
for col in ['TotalPremium', 'TotalClaims']:
    plt.figure(figsize=(8, 4))
    sns.boxplot(data=df, x=col)
    plt.title(f'Outliers in {col}')
    plt.tight_layout()
    plt.show()
