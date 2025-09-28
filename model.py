import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# Load cleaned data
df = pd.read_csv('cleaned_netflix_data.csv')

# Drop irrelevant columns (ID not useful for prediction)
df = df.drop(['customer_id'], axis=1)

# Separate features and target
X = df.drop('churned', axis=1)
y = df['churned']

# Identify categorical and numerical columns
categorical_cols = ['gender', 'subscription_type', 'region', 'device', 'payment_method', 'favorite_genre']
numerical_cols = ['age', 'watch_hours', 'last_login_days', 'monthly_fee', 'number_of_profiles', 'avg_watch_time_per_day']

# One-hot encode categoricals
X = pd.get_dummies(X, columns=categorical_cols, drop_first=True)  # drop_first avoids multicollinearity

# Scale numerical features
scaler = StandardScaler()
X[numerical_cols] = scaler.fit_transform(X[numerical_cols])

# Split into train/test (80/20, stratified for balance)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
print("Train shape:", X_train.shape, "Test shape:", X_test.shape)

from sklearn.linear_model import LogisticRegression
from xgboost import XGBClassifier

# Train Logistic Regression
log_reg = LogisticRegression(random_state=42)
log_reg.fit(X_train, y_train)

# Train XGBoost
xgb = XGBClassifier(random_state=42, eval_metric='logloss')
xgb.fit(X_train, y_train)
print("Models trained successfully!")

from sklearn.metrics import precision_score, recall_score, roc_auc_score, roc_curve
import matplotlib.pyplot as plt

# Function to evaluate a model
def evaluate_model(model, X_test, y_test, model_name):
    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]  # Churn probability
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    auc = roc_auc_score(y_test, y_prob)
    print(f"{model_name} - Precision: {precision:.4f}, Recall: {recall:.4f}, AUC: {auc:.4f}")
    
    # Plot ROC
    fpr, tpr, _ = roc_curve(y_test, y_prob)
    plt.plot(fpr, tpr, label=f'{model_name} (AUC = {auc:.4f})')
    
    return {'Precision': precision, 'Recall': recall, 'AUC': auc}

# Evaluate both
results = {}
results['Logistic Regression'] = evaluate_model(log_reg, X_test, y_test, 'Logistic Regression')
results['XGBoost'] = evaluate_model(xgb, X_test, y_test, 'XGBoost')

# Compare in a table
comparison_df = pd.DataFrame(results).T
print("\nModel Comparison:\n", comparison_df)

# Finalize ROC plot
plt.plot([0, 1], [0, 1], 'k--')  # Random line
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve Comparison')
plt.legend()
plt.show()

# Feature importance (for XGBoost, as it's more insightful)
importances = pd.DataFrame({'Feature': X.columns, 'Importance': xgb.feature_importances_})
importances = importances.sort_values('Importance', ascending=False).head(10)
print("\nTop 10 Features (XGBoost):\n", importances)

# Example: Predict churn probabilities on test set
test_probs = pd.DataFrame({'Churn_Probability': xgb.predict_proba(X_test)[:, 1]})
print("\nSample Predictions:\n", test_probs.head())  # Integrate with original data if needed

import joblib
joblib.dump(log_reg, 'log_reg_model.pkl')
joblib.dump(xgb, 'xgb_model.pkl')
joblib.dump(scaler, 'scaler.pkl')  # Save scaler for future preprocessing
print("Models and scaler saved!")