from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler
import io

app = FastAPI()

# CORS for frontend (if using React later)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:8501"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model and scaler
model = joblib.load('../xgb_model.pkl')
scaler = joblib.load('../scaler.pkl')

# Preprocess function
def preprocess_data(df):
    if 'customer_id' in df.columns:
        df = df.drop(['customer_id'], axis=1)
    if 'churned' in df.columns:
        df = df.drop(['churned'], axis=1)
    categorical_cols = ['gender', 'subscription_type', 'region', 'device', 'payment_method', 'favorite_genre']
    numerical_cols = ['age', 'watch_hours', 'last_login_days', 'monthly_fee', 'number_of_profiles', 'avg_watch_time_per_day']
    df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)
    training_columns = model.feature_names_in_
    for col in training_columns:
        if col not in df.columns:
            df[col] = 0
    df = df[training_columns]
    df[numerical_cols] = scaler.transform(df[numerical_cols])
    return df

# Suggest actions
def get_action(prob, row):
    if prob > 0.8:
        return "High risk: Offer 50% discount and personalized content push."
    elif prob > 0.6:
        if row.get('watch_hours', 0) < 5:
            return "Medium risk: Re-engage via email with binge-watch recommendations."
        else:
            return "Medium risk: Push premium content notifications."
    return "Low risk: No action needed."

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    df = pd.read_csv(io.BytesIO(await file.read()))
    original_df = df.copy()
    X = preprocess_data(df)
    probs = model.predict_proba(X)[:, 1]
    original_df['churn_probability'] = probs
    original_df['risk_level'] = original_df['churn_probability'].apply(lambda p: 'High' if p > 0.6 else 'Low')
    original_df['recommended_action'] = original_df.apply(lambda row: get_action(row['churn_probability'], row), axis=1)
    return {
        "all_subscribers": original_df.to_dict(orient='records'),
        "at_risk": original_df[original_df['churn_probability'] > 0.6].to_dict(orient='records')
    }