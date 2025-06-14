# Task 3: Statistical Validation of Risk Drivers

This report summarizes the hypothesis tests conducted to evaluate key risk factors influencing claim frequency 
and profitability. The goal is to determine whether significant differences exist across various segments, 
informing strategic decisions for underwriting, pricing, and risk management.

---

## 1. Impact of Gender on Claim Frequency

### Hypotheses:
- **Null Hypothesis (H₀):** There is no difference in claim frequency between male and female clients.
- **Alternative Hypothesis (H₁):** A difference exists in claim frequency between male and female clients.

### Method:
- **Test Used:** Welch’s t-test (assumes unequal variance)
- **Sample Metric:** Claim frequency (binary: claimed or not)
- **Groups Compared:** Male vs Female clients

### Results:
- **T-statistic:** 0.2055
- **P-value:** 0.8372

### Interpretation:
Since the p-value exceeds 0.05, we **fail to reject the null hypothesis**. This indicates that gender does 
not have a statistically significant effect on the likelihood of filing a claim.

### Business Implication:
ACIS should not consider gender as a segmentation variable for risk prediction or marketing strategies. 
The findings support gender neutrality in underwriting, promoting fairness and inclusivity.

---

## 2. Risk Differences Across Provinces on Claim Frequency

### Hypotheses:
- **Null Hypothesis (H₀):** There are no risk differences across provinces; claim frequency is independent 
     of province.
- **Alternative Hypothesis (H₁):** Claim frequency varies significantly across provinces.

### Method:
- **Test Used:** Chi-squared test of independence
- **Contingency Table:** Province (9 regions) vs Claim (Yes/No)

### Results:
- **Chi-squared Statistic:** 104.1909
- **Degrees of Freedom:** 8
- **P-value:** < 0.0001

### Conclusion:
We **reject H₀**, indicating a significant association between province and claim frequency.

### Business Implication:
There is strong evidence that claim frequency varies across regions. Notably:
- Gauteng and KwaZulu-Natal exhibit higher claim rates than expected.
- Eastern Cape and Free State show fewer claims than anticipated.

**Recommended Action:** Adjust premiums regionally to reflect varying risk levels, potentially 
  improving underwriting accuracy and reducing overall loss ratios.

---

## 3. Summary of Hypothesis Tests

| Hypothesis                                  | Test Used     | P-value      | Decision             | Business Insight                                                |
|---------------------------------------------|---------------|--------------|----------------------|----------------------------------------------------------------|
| No risk difference across provinces         | Chi-squared   | < 0.0001     | Reject               | Adjust premiums based on provincial risk profiles             |
| No risk difference between ZIP codes        | Chi-squared   | < 0.0001     | Reject               | Consider ZIP-based underwriting adjustments                     |
| No margin difference between ZIP codes      | T-test        | 0.2445       | Fail to reject       | Uniform margins across ZIP codes are acceptable               |
| No risk difference between Men and Women    | T-test        | 0.8372       | Fail to reject       | Gender-based premium differentiation is unnecessary           |

---

## **Summary & Recommendations**

The analysis reveals significant regional risk variations but no statistically significant differences based on 
gender or between specific ZIP codes regarding claim frequency and margin. 

**Key Takeaways:**
- Implement regional premium adjustments in high-risk provinces.
- Maintain gender-neutral underwriting policies.
- Further analysis could explore other potential risk factors.

This evidence-based approach will enable ACIS to optimize pricing strategies, improve risk segmentation, and 
enhance overall profitability.
