import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import shap

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, precision_score, recall_score, f1_score, classification_report

import lightgbm as lgb

# -----------------------------
# Settings
# -----------------------------
DATA_PATH = 'processed/cleaned_train_set.csv'
OUTPUT_DIR = 'outputs'
os.makedirs(OUTPUT_DIR, exist_ok=True)

USE_SAMPLE = True  # Toggle for speed
SAMPLE_FRAC = 0.1

# -----------------------------
# Load Data
# -----------------------------
print("Loading data...")
data = pd.read_csv(DATA_PATH, low_memory=False)
if USE_SAMPLE:
    print(f"Sampling {SAMPLE_FRAC*100}% of data for speed...")
    data = data.sample(frac=SAMPLE_FRAC, random_state=42)
print("✅ Data loaded.")
print("Columns:", data.columns.tolist())

# -----------------------------
# Prepare targets
# -----------------------------
regression_target = 'TotalClaims'

# Handle TotalPremium
if data['TotalPremium'].dtype == object:
    data['TotalPremium'] = pd.to_numeric(data['TotalPremium'], errors='coerce')

median_premium = data['TotalPremium'].median()
data['is_high_premium'] = (data['TotalPremium'] > median_premium).astype(int)
classification_target = 'is_high_premium'

# Drop rows with missing targets
data = data.dropna(subset=[regression_target, 'TotalPremium'])

# -----------------------------
# Handle date columns
# -----------------------------
date_cols = []
for col in data.select_dtypes(include='object').columns:
    try:
        pd.to_datetime(data[col])
        date_cols.append(col)
    except:
        pass

for col in date_cols:
    parsed = pd.to_datetime(data[col], errors='coerce')
    data[col + '_year'] = parsed.dt.year
    data[col + '_month'] = parsed.dt.month
    data[col + '_day'] = parsed.dt.day
    data.drop(columns=[col], inplace=True)

# -----------------------------
# Encode categoricals
# -----------------------------
for col in data.select_dtypes(include='object').columns:
    data[col] = data[col].astype('category').cat.codes

# Fill missing values
data.fillna(0, inplace=True)

# -----------------------------
# Features and targets
# -----------------------------
excluded_cols = ['UnderwrittenCoverID', 'PolicyID']
features = [col for col in data.columns if col not in [regression_target, classification_target] + excluded_cols]
X = data[features]
y_reg = data[regression_target]
y_clf = data[classification_target]

# -----------------------------
# Train/test split
# -----------------------------
X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(X, y_reg, test_size=0.2, random_state=42)
X_train_clf, X_test_clf, y_train_clf, y_test_clf = train_test_split(X, y_clf, test_size=0.2, random_state=42)

print(f"\nShapes:")
print(f"  Regression train: {X_train_reg.shape}")
print(f"  Regression test: {X_test_reg.shape}")
print(f"  Classification train: {X_train_clf.shape}")
print(f"  Classification test: {X_test_clf.shape}")

# -----------------------------
# Regression with LightGBM
# -----------------------------
print("\n🔧 Training regression model with LightGBM...")
lgb_reg = lgb.LGBMRegressor(n_jobs=-1, random_state=42)
lgb_reg.fit(X_train_reg, y_train_reg)
y_pred_reg = lgb_reg.predict(X_test_reg)

rmse = np.sqrt(mean_squared_error(y_test_reg, y_pred_reg))
r2 = r2_score(y_test_reg, y_pred_reg)

print(f"\n📈 Regression Results:\n  RMSE: {rmse:.2f}\n  R²: {r2:.2f}")

# Feature importance plot
importances = lgb_reg.feature_importances_
indices = np.argsort(importances)[::-1]
plt.figure(figsize=(10, 6))
plt.title("🔍 Regression Feature Importance (LightGBM)")
plt.bar(range(len(importances)), importances[indices], align="center")
plt.xticks(range(len(importances)), [features[i] for i in indices], rotation=90)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "lgbm_regression_feature_importance.png"))

# SHAP for regression
print("\n🔍 Computing SHAP values for regression...")
explainer_reg = shap.TreeExplainer(lgb_reg)
shap_values_reg = explainer_reg.shap_values(X_test_reg)
shap.summary_plot(shap_values_reg, X_test_reg, plot_type="bar", show=False)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "shap_summary_regression_lgbm.png"))

# -----------------------------
# Classification with LightGBM
# -----------------------------
print("\n🔧 Training classification model with LightGBM...")
lgb_clf = lgb.LGBMClassifier(n_jobs=-1, random_state=42)
lgb_clf.fit(X_train_clf, y_train_clf)
y_pred_clf = lgb_clf.predict(X_test_clf)

# Metrics
accuracy = accuracy_score(y_test_clf, y_pred_clf)
precision = precision_score(y_test_clf, y_pred_clf)
recall = recall_score(y_test_clf, y_pred_clf)
f1 = f1_score(y_test_clf, y_pred_clf)

print(f"\n✅ Classification Results:")
print(f"  Accuracy:  {accuracy:.2f}")
print(f"  Precision: {precision:.2f}")
print(f"  Recall:    {recall:.2f}")
print(f"  F1-score:  {f1:.2f}")
print(classification_report(y_test_clf, y_pred_clf))

# Feature importance plot
importances_clf = lgb_clf.feature_importances_
indices_clf = np.argsort(importances_clf)[::-1]
plt.figure(figsize=(10, 6))
plt.title("🔍 Classification Feature Importance (LightGBM)")
plt.bar(range(len(importances_clf)), importances_clf[indices_clf], align="center")
plt.xticks(range(len(importances_clf)), [features[i] for i in indices_clf], rotation=90)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "lgbm_classification_feature_importance.png"))

# SHAP for classification
print("\n🔍 Computing SHAP values for classification...")
explainer_clf = shap.TreeExplainer(lgb_clf)
shap_values_clf = explainer_clf.shap_values(X_test_clf)

if isinstance(shap_values_clf, list):
    # For binary classification, shap_values_clf[1]
    shap.summary_plot(shap_values_clf[1], X_test_clf, plot_type="bar", show=False)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "shap_summary_classification_lgbm.png"))
else:
    print("⚠️ SHAP output is not a list. Skipping plot.")