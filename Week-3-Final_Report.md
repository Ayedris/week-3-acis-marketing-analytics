# Week 3 Final Report: ACIS Car Insurance Risk Analytics & Pricing Optimization

## Overview

This report summarizes the work completed during Week 3 of the 10Academy AI Mastery Program. The client, **AlphaCare Insurance Solutions (ACIS)**, is a car insurance provider in South Africa seeking to optimize its pricing strategy and marketing efforts using advanced data analytics and machine learning.

Our project was divided into four key tasks:

1. Exploratory Data Analysis (EDA)
2. Reproducible Data Pipeline with DVC
3. Hypothesis Testing & Segmentation Strategy
4. Predictive Modeling & Interpretability

---
# Week 3 Final Report: ACIS Car Insurance Risk Analytics & Pricing Optimization

##  Overview

This report summarizes the work completed during Week 3 of the 10Academy AI Mastery Program. The client, **AlphaCare Insurance Solutions (ACIS)**, is a car insurance provider in South Africa seeking to optimize its pricing strategy and marketing efforts using advanced data analytics and machine learning.

Our project was divided into four key tasks:

1. Exploratory Data Analysis (EDA)  
2. Reproducible Data Pipeline with DVC  
3. Hypothesis Testing & Segmentation Strategy  
4. Predictive Modeling & Interpretability  

---

##  Task 1: Exploratory Data Analysis (EDA)

We performed univariate and multivariate analyses to understand the underlying patterns in the dataset.

### Key Insights:

- **High number of zero-claim customers**: Suggests many low-risk clients.
- **Correlations**:
  - Strong positive correlation between vehicle age and claim severity.
  - Negative correlation between driver age and claim count.

###  Plots to Include:

1. `Creative_Insightful_Plots/correlation_matrix.png`: Correlation heatmap  
2. `Creative_Insightful_Plots/vehicle_age_vs_claims.png`: Vehicle age vs. claims  
3. `Creative_Insightful_Plots/age_vs_claims.png`: Driver age vs. claims  

---

## ⚙️ Task 2: Data Pipeline with DVC

We implemented a **reproducible data pipeline** using DVC to ensure version-controlled and auditable workflows.

### Key Steps:

- Created `dvc.yaml` to define the pipeline stages  
- Tracked raw data, cleaned data, and script dependencies  
- Used `.gitignore` to avoid large files being pushed  

> This setup ensures that any teammate can reproduce results with a single `dvc repro` command.


##  Task 3: Hypothesis Testing & Segmentation Strategy

We statistically tested key hypotheses to segment customers into risk categories and support data-driven pricing policies.

### Hypotheses Tested:

1. **Gender-based Claim Risk**  
   ➤ No significant difference in claim frequency between men and women (p = 0.8372).

2. **Risk Differences Across Provinces**  
   ➤ Significant difference in claim frequency across provinces (p < 0.0001).

3. **ZIP Code (PostalCode) vs. Claim and Margin**  
   ➤ Risk difference across ZIP codes (PostalCode) is significant, but margin differences are not.

### Techniques Used:

- Chi-squared tests  
- Welch’s t-tests  
- Boxplots  

###  Plots to Include:

4. `Exploratory-Data-Analysis/chi_square_residence_area.png`: Chi-squared test – residence area vs. claim frequency  
5. `Exploratory-Data-Analysis/boxplot_claims_by_province.png`: Boxplot – claim frequency by province  

### Key Findings:

- **Residence Area:** Urban areas are associated with higher claim frequency.  
- **Gender:** Gender has no significant effect on claim frequency — supports fairness in underwriting.  
- **Geography:** Province and ZIP code significantly affect risk — enabling location-based premium adjustment.  

### Business Implications:

- Implement **region-specific pricing strategies**.  
- Maintain **gender-neutral underwriting** for fairness and compliance.  
- Explore additional segmentation using vehicle and driver profiles.  

##  Task 4: Predictive Modeling & Interpretability

We built two types of models:

1. **Regression (Claim Severity)**  
2. **Classification (Claim Risk)**  

### Models Used:

- Linear Regression  
- Lasso Regression  
- LightGBM Regression  
- Logistic Regression  
- Random Forest Classifier  
- LightGBM Classifier  

###  Evaluation Metrics:

- **Regression**: RMSE, R²  
- **Classification**: Accuracy, Precision, Recall, F1-score  

###  Plots to Include:

6. `outputs/lgbm_regression_feature_importance.png`: Regression model feature importances  
7. `outputs/lgbm_classification_feature_importance.png`: Classification model feature importances  
8. `outputs/shap_summary_regression_lgbm.png`: SHAP values for regression  

### Key Findings:

- LightGBM models outperformed linear models significantly.  
- Top features for severity prediction: Vehicle age, driver experience, vehicle value.  
- SHAP revealed that higher vehicle age and lower driver experience increase predicted severity.  


##  Summary of Business Recommendations

- **Premium Discounts**: Offer to low-risk groups (e.g., older drivers, newer vehicles).  
- **Marketing Focus**: Target high-premium regions with better conversion rates.  
- **Policy Adjustments**: Adjust rates for vehicle age and residence area based on insights.  
- **Ongoing Analytics**: Maintain DVC pipeline for reproducibility and future model updates.  

---

##  Files in This Report

- `Task-1-summary.md`  
- `Task-3-report.md`  
- `Task-4-summary.md`  
- 📁 `outputs/*.png` (listed above)

---

##  Final Thoughts

This challenge highlighted the importance of both statistical reasoning and machine learning in building intelligent pricing systems. We successfully delivered actionable insights and interpretable models for ACIS to optimize their car insurance strategy.

> Thank you 10Academy for the opportunity!


**Author**: Ahmed Muhammed Edris  
**Program**: 10Academy AI Mastery – Week 3 Challenge  
**Date**: June 2025

## Task 3: Hypothesis Testing & Segmentation Strategy

We statistically tested key hypotheses to segment customers into risk categories.

### Hypotheses:

1. Customers from urban areas have higher claim frequencies.
2. Older vehicles are associated with more severe claims.
3. Married customers file fewer claims on average.

### Techniques:

* ANOVA
* Chi-squared tests
* Boxplots

###  Plots to Include:

4. `Exploratory-Data-Analysis/anova_claims_vehicle_age.png`: ANOVA vehicle age vs. severity
5. `Exploratory-Data-Analysis/chi_square_residence_area.png`: Residence area vs. claim frequency

### Key Findings:

* Statistically significant differences in claim severity across vehicle age groups.
* Strong relationship between residence area and claim frequency.

---

## 🤖 Task 4: Predictive Modeling & Interpretability

We built two types of models:

1. **Regression (Claim Severity)**
2. **Classification (Claim Risk)**

### Models Used:

* Linear Regression
* Lasso Regression
* LightGBM Regression
* Logistic Regression
* Random Forest Classifier
* LightGBM Classifier

###  Evaluation Metrics:

* **Regression**: RMSE, R²
* **Classification**: Accuracy, Precision, Recall, F1-score

###  Plots to Include:

6. `outputs/lgbm_regression_feature_importance.png`: Regression model feature importances
7. `outputs/lgbm_classification_feature_importance.png`: Classification model feature importances
8. `outputs/shap_summary_regression_lgbm.png`: SHAP values for regression

### Key Findings:

* LightGBM models outperformed linear models significantly.
* Top features for severity prediction: Vehicle age, driver experience, vehicle value.
* SHAP revealed that higher vehicle age and lower driver experience increase predicted severity.

---

##  Summary of Business Recommendations

* **Premium Discounts**: Offer to low-risk groups (e.g., older drivers, newer vehicles).
* **Marketing Focus**: Target high-premium regions with better conversion rates.
* **Policy Adjustments**: Adjust rates for vehicle age and residence area based on insights.
* **Ongoing Analytics**: Maintain DVC pipeline for reproducibility and future model updates.

---

##  Files in This Report

* `Task-1-summary.md`
* `Task-3-report.md`
* `Task-4-summary.md`
*  `outputs/*.png` (listed above)


##  Final Thoughts

This challenge highlighted the importance of both statistical reasoning and machine learning in building intelligent pricing systems. We successfully delivered actionable insights and interpretable models for ACIS to optimize their car insurance strategy.

> Thank you 10Academy for the opportunity!


Author: Ahmed Muhammed Edris
Program: 10Academy AI Mastery – Week 3 Challenge
Date: June 2025
