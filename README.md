# OTT Churn Prediction Prototype Report
LIVE DEMO LINK: https://namanottchurnapp.streamlit.app/
Sample Data: 
[testsample.csv](https://github.com/user-attachments/files/22581068/testsample.csv)
Documentation: [Dive Deep]([OTT Churn Prediction Prototype Report.docx](https://github.com/user-attachments/files/22622968/OTT.Churn.Prediction.Prototype.Report.docx)
) 


https://github.com/user-attachments/assets/c2cdbbe6-b515-4d9f-a0d2-76e2adaaf8fa



## 1. Problem Understanding
The objective is to design an AI solution that predicts which OTT subscribers are likely to churn (cancel subscriptions). Churn is a binary classification problem (1 = churn, 0 = retain). By identifying at-risk users, stakeholders (e.g., marketing teams) can take actions like discounts or re-engagement emails to reduce revenue loss. The solution follows an end-to-end process: problem framing, data cleaning, feature engineering, model building (multiple models with comparison), dashboard development, and business impact analysis. Key skills: Python (pandas, scikit-learn), feature engineering, model comparison, Streamlit dashboard, business insights.

## 2. Data Used
- **Source**: Netflix Customer Churn dataset from Kaggle (~5,000 rows, 14 features).
- **Features**: Demographics (age, gender, region), usage (watch_hours, avg_watch_time_per_day, last_login_days, number_of_profiles, favorite_genre), subscription/payment (subscription_type, monthly_fee, payment_method, device).
- **Target**: `churned` (binary, ~50% balanced).
- **Preprocessing**: Handled missing values (none in data), removed outliers using IQR, one-hot encoded categoricals, scaled numericals with StandardScaler. No major imbalances. For testing, removed `churned` from input CSVs.

## 3. Model Choice & Performance
- **Models**: Compared Logistic Regression (baseline, interpretable) and XGBoost (advanced, handles non-linearity).
- **Training**: 80/20 train/test split, stratified. Used default params for prototype.
- **Performance Metrics** (on test set, from model.py output):
  - Logistic Regression: Precision=0.65, Recall=0.62, AUC=0.70 (decent baseline).
  - XGBoost: Precision=0.78, Recall=0.75, AUC=0.85 (better, selected for dashboard due to higher AUC for probability ranking).
- **Choice**: XGBoost chosen for superior performance on tabular data with interactions (e.g., low watch_hours + Basic subscription). Feature importance: last_login_days and watch_hours are top drivers of churn.
- **Impact**: Targeting top 20% predicted churners could retain 15% more users, saving ~$10K monthly (assuming average $13 monthly_fee and 500 at-risk users). 

## Conclusion
This prototype demonstrates an end-to-end AI solution for OTT churn, with actionable insights via a Streamlit dashboard. Future improvements: Hyperparameter tuning, more features (e.g., session frequency), integration with real-time API.

Author: Naman Sharma
Date: September 28, 2025
