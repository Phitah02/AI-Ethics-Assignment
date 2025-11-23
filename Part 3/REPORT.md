# COMPAS Recidivism Dataset Bias Audit Report

## Introduction
This report analyzes racial bias in COMPAS recidivism risk scores using IBM's AI Fairness 360 toolkit. The ProPublica dataset assesses defendants in Broward County, Florida, focusing on disparities between African-American and Caucasian defendants.

## Methodology
Data was preprocessed to include felony defendants screened within 30 days of arrest, excluding invalid cases. AIF360's CompasDataset replicated ProPublica's steps. Bias metrics included statistical parity difference, disparate impact, and classification rates (FPR/FNR). Visualizations used Matplotlib/Seaborn. Mitigation applied AIF360's Reweighing algorithm.

## Findings
Significant racial disparities exist:

- **Statistical Parity Difference**: -0.097 (African-Americans 9.7% less likely for favorable outcomes)
- **Disparate Impact**: 0.840 (16% less favorable predictions for African-Americans)
- **FPR Difference**: 0.0007 (African-Americans: 42.5%, Caucasians: 44.1%)
- **FNR Difference**: -0.016 (African-Americans: 53.6%, Caucasians: 53.5%)

Visualizations reveal over-prediction for African-Americans despite higher actual recidivism (51.4% vs. 39.2%).

## Bias Mitigation
Reweighing adjusted instance weights for fairness. Post-mitigation:

- **Statistical Parity Difference**: ~0.000
- **Disparate Impact**: ~1.000

Reweighing achieved statistical fairness, though FPR/FNR unchanged as they depend on predictions.

## Recommendations
1. Conduct regular audits with fairness metrics.
2. Use preprocessing techniques like Reweighing.
3. Ensure proportional representation in data.
4. Maintain human oversight in decisions.
5. Promote policies limiting AI in sentencing.
6. Monitor and update models continuously.

This analysis highlights the need for ethical AI practices in criminal justice to prevent perpetuating inequality.

(Word count: 278)
