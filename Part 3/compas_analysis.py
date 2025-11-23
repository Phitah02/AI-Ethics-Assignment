import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from aif360.datasets import CompasDataset
from aif360.metrics import BinaryLabelDatasetMetric, ClassificationMetric
from aif360.algorithms.preprocessing import Reweighing
from sklearn.metrics import confusion_matrix

# Set style
sns.set(style='whitegrid')

# Load dataset
dataset_orig = CompasDataset()

# Load raw data for decile_score
raw_df = pd.read_csv('compas-scores-two-years.csv')
raw_df = raw_df.dropna(subset=["days_b_screening_arrest"])
raw_df = raw_df[(raw_df.days_b_screening_arrest <= 30) & (raw_df.days_b_screening_arrest >= -30) & (raw_df.is_recid != -1) & (raw_df.c_charge_degree != "O") & (raw_df.score_text != "N/A")]
print("raw_df shape after filter:", raw_df.shape)

# Convert to dataframe for easier manipulation
df = dataset_orig.convert_to_dataframe()[0]
df['decile_score'] = raw_df['decile_score'].values[:len(df)]
print("Dataset loaded. Shape:", df.shape)
print("Feature names:", dataset_orig.feature_names[:10])  # first 10
print('decile_score in df:', 'decile_score' in df.columns)
print(df.head())

# Define privileged and unprivileged groups
# Privileged: Caucasian (race=1), Unprivileged: African-American (race=0)
privileged_groups = [{'race': 1}]
unprivileged_groups = [{'race': 0}]

# Target variable is 'two_year_recid' (recidivated within 2 years)
# Favorable label is 0 (no recidivism), unfavorable is 1
favorable_label = 0
unfavorable_label = 1

# Compute dataset metrics
metric_orig = BinaryLabelDatasetMetric(dataset_orig,
                                       unprivileged_groups=unprivileged_groups,
                                       privileged_groups=privileged_groups)

print("Statistical Parity Difference:", metric_orig.statistical_parity_difference())
print("Disparate Impact:", metric_orig.disparate_impact())
print("Mean Difference:", metric_orig.mean_difference())

# For classification metrics, we need predicted labels
# In COMPAS, the decile_score is the prediction
# Threshold at 5 for high risk
threshold = 5
dataset_orig_pred = dataset_orig.copy()
dataset_orig_pred.labels = (df['decile_score'] >= threshold).astype(int)

# Classification metrics
classified_metric = ClassificationMetric(dataset_orig, dataset_orig_pred,
                                         unprivileged_groups=unprivileged_groups,
                                         privileged_groups=privileged_groups)

print("False Positive Rate Difference:", classified_metric.false_positive_rate_difference())
print("False Negative Rate Difference:", classified_metric.false_negative_rate_difference())
print("Equal Opportunity Difference:", classified_metric.equal_opportunity_difference())

# Prepare data for plotting
df_plot = df.copy()
df_plot['race_label'] = df_plot['race'].map({0: 'African-American', 1: 'Caucasian'})
df_plot['predicted_high_risk'] = (df_plot['decile_score'] >= threshold).astype(int)
df_plot['recidivated'] = df_plot['two_year_recid']

# Confusion matrix by race
cm_aa = confusion_matrix(df_plot[df_plot['race'] == 0]['recidivated'], df_plot[df_plot['race'] == 0]['predicted_high_risk'])
cm_c = confusion_matrix(df_plot[df_plot['race'] == 1]['recidivated'], df_plot[df_plot['race'] == 1]['predicted_high_risk'])

# Calculate rates
tn_aa, fp_aa, fn_aa, tp_aa = cm_aa.ravel()
tn_c, fp_c, fn_c, tp_c = cm_c.ravel()

fpr_aa = fp_aa / (fp_aa + tn_aa)
fpr_c = fp_c / (fp_c + tn_c)
fnr_aa = fn_aa / (fn_aa + tp_aa)
fnr_c = fn_c / (fn_c + tp_c)

print(f"African-American FPR: {fpr_aa:.3f}, Caucasian FPR: {fpr_c:.3f}")
print(f"African-American FNR: {fnr_aa:.3f}, Caucasian FNR: {fnr_c:.3f}")

# Plot FPR and FNR disparities
races = ['African-American', 'Caucasian']
fpr_values = [fpr_aa, fpr_c]
fnr_values = [fnr_aa, fnr_c]

fig, ax = plt.subplots(1, 2, figsize=(12, 5))

ax[0].bar(races, fpr_values, color=['red', 'blue'])
ax[0].set_title('False Positive Rate by Race')
ax[0].set_ylabel('FPR')

ax[1].bar(races, fnr_values, color=['red', 'blue'])
ax[1].set_title('False Negative Rate by Race')
ax[1].set_ylabel('FNR')

plt.tight_layout()
plt.savefig('fpr_fnr_disparity.png')
plt.show()

# Plot actual vs predicted recidivism by race
recid_by_race = df_plot.groupby('race_label')['recidivated'].mean()
predicted_by_race = df_plot.groupby('race_label')['predicted_high_risk'].mean()

fig, ax = plt.subplots(figsize=(8, 5))
width = 0.35
x = np.arange(len(races))

ax.bar(x - width/2, recid_by_race.values, width, label='Actual Recidivism', color='orange')
ax.bar(x + width/2, predicted_by_race.values, width, label='Predicted High Risk', color='green')

ax.set_xlabel('Race')
ax.set_ylabel('Proportion')
ax.set_title('Actual vs Predicted Recidivism by Race')
ax.set_xticks(x)
ax.set_xticklabels(races)
ax.legend()

plt.savefig('recidivism_comparison.png')
plt.show()

# Apply Reweighing
RW = Reweighing(unprivileged_groups=unprivileged_groups,
                privileged_groups=privileged_groups)
dataset_transf = RW.fit_transform(dataset_orig)

# Compute metrics after mitigation
metric_transf = BinaryLabelDatasetMetric(dataset_transf,
                                         unprivileged_groups=unprivileged_groups,
                                         privileged_groups=privileged_groups)

print("After Reweighing:")
print("Statistical Parity Difference:", metric_transf.statistical_parity_difference())
print("Disparate Impact:", metric_transf.disparate_impact())
print("Mean Difference:", metric_transf.mean_difference())

# For classification, apply same threshold
dataset_transf_pred = dataset_transf.copy()
dataset_transf_pred.labels = (dataset_transf.features[:, dataset_transf.feature_names.index('decile_score')] >= threshold).astype(int)

classified_metric_transf = ClassificationMetric(dataset_transf, dataset_transf_pred,
                                                unprivileged_groups=unprivileged_groups,
                                                privileged_groups=privileged_groups)

print("False Positive Rate Difference:", classified_metric_transf.false_positive_rate_difference())
print("False Negative Rate Difference:", classified_metric_transf.false_negative_rate_difference())
print("Equal Opportunity Difference:", classified_metric_transf.equal_opportunity_difference())