import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('netflix_customer_churn.csv')  # Adjust path if needed
print("First 5 rows:\n", df.head())
print("\nData Info:\n", df.info())
print("\nSummary Stats:\n", df.describe())
print("\nMissing Values:\n", df.isnull().sum())

# Unique Values in Categoricals (Fixed with your column names)
print("\nUnique Values in Categoricals:")
for col in ['subscription_type', 'region', 'gender', 'device', 'payment_method', 'favorite_genre']:
    print(f"{col}: {df[col].unique()}")

#Handle missing values
for col in ['monthly_fee', 'watch_hours', 'avg_watch_time_per_day', 'age']:
    df[col].fillna(df[col].median(), inplace=True)

for col in ['subscription_type', 'region', 'gender', 'device', 'payment_method', 'favorite_genre']:
    df[col].fillna(df[col].mode()[0] if not df[col].mode().empty else 'Unknown', inplace=True)
if df['churned'].isnull().sum() > 0:
    df = df.dropna(subset=['churned'])
print("\nMissing Values After Cleaning:\n", df.isnull().sum())

# Convert Data Types (Churn already int; no dates here)
if df['churned'].dtype == 'object':
    df['churned'] = df['churned'].map({'Yes': 1, 'No': 0})
for col in ['subscription_type', 'region', 'gender', 'device', 'payment_method', 'favorite_genre']:
    df[col] = df[col].astype(str)
print("\nData Types After Conversion:\n", df.dtypes)


# Remove Duplicates and Outliers
df = df.drop_duplicates(subset=['customer_id'])
print(f"\nShape After Removing Duplicates: {df.shape}")

# Remove outliers using IQR for key numerical columns
numerical_cols = ['watch_hours', 'monthly_fee', 'avg_watch_time_per_day', 'last_login_days']
for col in numerical_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    original_shape = df.shape[0]
    df = df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]
    print(f"Removed {original_shape - df.shape[0]} outliers from {col}")
print(f"\nShape After Removing Outliers: {df.shape}")

# Exploratory Data Analysis (EDA)
# Distributions of numerical features
for col in ['watch_hours', 'monthly_fee', 'age', 'avg_watch_time_per_day']:
    plt.figure(figsize=(8, 4))
    sns.histplot(df[col], kde=True)
    plt.title(f'Distribution of {col}')
    plt.show()

# Churn rate by subscription_type (example categorical)
plt.figure(figsize=(8, 4))
sns.countplot(x='subscription_type', hue='churned', data=df)
plt.title('Churn by Subscription Type')
plt.show()

# Check class balance
print("\nChurn Distribution:\n", df['churned'].value_counts(normalize=True))

# Save Cleaned Data
df.to_csv('cleaned_netflix_data.csv', index=False)
print("\nCleaned data saved as 'netflix_customer_churn.csv'")
