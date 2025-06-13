# Task 1 Insights Summary: Exploratory Data Analysis for AlphaCare Insurance Solutions

## Overview

This report presents key exploratory insights derived from the cleaned historical insurance data, as part of Week 3 Task 1 for AlphaCare Insurance Solutions (ACIS). The goal was to uncover patterns that will inform risk assessment and marketing strategy in the car insurance domain.

---

## 1. Overall Portfolio Loss Ratio

* **Definition**: Loss Ratio = Total Claims / Total Premium
* **Computed Value**: **1.05**

  * This indicates that, on average, claim payouts are slightly exceeding collected premiums, suggesting **unprofitability** and potential pricing or risk issues.

---

## 2. Loss Ratio Analysis by Key Demographics

### a) By Province:

Top provinces with **highest loss ratios**:

* **Gauteng**
* **KwaZulu-Natal**
* **Western Cape**

These regions may require re-evaluation in underwriting, pricing, or risk management strategies.

### b) By Gender:

* Female and Male groups show slight differences in loss ratio, but further statistical tests would be needed to confirm significant disparities.

### c) By Vehicle Type:

* Variability observed in loss ratios across vehicle types (e.g., **Minibus**, **SUV**, **Sedan**), indicating the need for type-specific premium calibration.

---

## 3. Financial Variables: Outlier Detection

* **Boxplot analysis** revealed notable outliers in:

  * **TotalClaims**: Right-skewed with high-magnitude extreme claims.
  * **CustomValueEstimate**: Broad range with many high-value vehicles.
* Recommendation: Apply **outlier handling** (e.g., winsorization or log transformation) in downstream modeling tasks to reduce skew.

---

## 4. Temporal Trends in Claims

* Time period covered: **Feb 2014 to Aug 2015**

### a) Monthly Average Claim per Policy

* Notable peaks observed in:

  * **March 2014**
  * **December 2014**
  * **April 2015**

These spikes may correspond to seasonal trends, economic changes, or external events affecting claim volumes/severity.

---

## 5. Vehicle Makes with Extreme Claim Averages

### a) Highest Average Claim Amounts:

* **SUZUKI**, **JMC**, **HYUNDAI**, **MARCOPOLO**, **AUDI** — indicate higher relative risk.

### b) Zero Average Claim Amounts:

* **HINO**, **JINBEI**, **LEXUS**, **PEUGEOT**, **VOLVO**, etc.

  * Some of these may have **low sample sizes** or genuinely low claim history.

Recommendation: Further explore these vehicle makes/models in context of frequency, volume, and coverage levels.

---

## Conclusion

The insights uncovered provide a solid foundation for defining risk clusters, adjusting pricing, and targeting low-risk customers. The next step will involve feature engineering and model development to quantify and leverage these findings in predictive analytics.

Prepared by: Ahmed Muhammed Edris
Date: June 12, 2025
