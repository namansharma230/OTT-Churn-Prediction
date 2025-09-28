[testsample.csv](https://github.com/user-attachments/files/22581068/testsample.csv)# OTT Churn Prediction Prototype Report
LIVE DEMO LINK: https://namanottchurnapp.streamlit.app/
Sample Data: [Uplcustomer_id,age,gender,subscription_type,watch_hours,last_login_days,region,device,monthly_fee,churned,payment_method,number_of_profiles,avg_watch_time_per_day,favorite_genre
a9b75100-82a8-427a-a208-72f24052884a,51,Other,Basic,14.73,29,Africa,TV,8.99,1,Gift Card,1,0.49,Action
49a5dfd9-7e69-4022-a6ad-0a1b9767fb5b,47,Other,Standard,0.7,19,Europe,Mobile,13.99,1,Gift Card,5,0.03,Sci-Fi
d3c72c38-631b-4f9e-8a0e-de103cad1a7d,53,Other,Premium,4.51,12,Oceania,TV,17.99,1,Crypto,2,0.35,Horror
4e265c34-103a-4dbb-9553-76c9aa47e946,56,Other,Standard,1.89,13,Africa,Mobile,13.99,1,Crypto,2,0.13,Action
d8079475-5be7-47e9-8782-ceb7ff61395e,58,Female,Standard,13.8,26,Oceania,Mobile,13.99,0,Debit Card,3,0.51,Action
8e63450a-13d6-4e83-bbb5-6aebde9152cb,48,Other,Basic,13.83,20,Asia,TV,8.99,0,Gift Card,5,0.66,Romance
02387681-8c42-462a-807a-de0168c73b38,51,Male,Basic,14.3,56,Europe,Mobile,8.99,1,Gift Card,1,0.25,Action
0bcaad0c-545c-4ee1-85a6-75e165f39361,45,Other,Basic,9.98,10,Asia,Mobile,8.99,0,PayPal,3,0.91,Romance
eae6439e-8cdf-4258-ab49-c493925b927a,32,Other,Premium,2.22,34,Europe,TV,17.99,1,Debit Card,1,0.06,Drama
45a03ce3-26d0-4cd5-a9bd-22d42490b612,26,Male,Premium,15.42,36,Asia,Laptop,17.99,0,Debit Card,4,0.42,Comedy
9df43ad1-d6ee-44d0-a79b-c8ab444f10bf,28,Other,Standard,22.26,38,South America,Mobile,13.99,0,Crypto,5,0.57,Horror
4690bf9c-b828-44d3-bdb6-f91b10668288,47,Other,Standard,7.92,23,South America,TV,13.99,0,Crypto,1,0.33,Sci-Fi
0aac0e54-7d40-4cf2-abe4-45f3ff73f5ff,49,Female,Basic,5.26,33,South America,Mobile,8.99,1,Crypto,3,0.15,Documentary
e2a75072-5f48-47ed-a533-eb1b0301aad9,39,Female,Basic,10.97,10,Oceania,Mobile,8.99,0,PayPal,1,1,Comedy
bf48551e-a8e6-4fd9-bb32-3f798ed84680,46,Other,Premium,1.25,13,Europe,Tablet,17.99,1,Debit Card,3,0.09,Comedy
3819aaed-bed6-49c8-ab53-0fd9d917e4e1,48,Female,Standard,8.12,32,Africa,Desktop,13.99,1,Crypto,2,0.25,Action
e2f28860-44e4-4fc2-a445-014332e7fb11,68,Female,Premium,7.67,40,Oceania,Tablet,17.99,0,PayPal,4,0.19,Romance
a088d61d-be5a-409e-b943-73b145b358d1,21,Female,Standard,15.53,27,South America,Laptop,13.99,0,Credit Card,1,0.55,Comedy
a8c8dcff-92d3-4a79-849d-42c6e6bbc7bc,70,Other,Premium,7.97,57,Europe,Laptop,17.99,1,Gift Card,5,0.14,Drama
18be905c-203f-4de2-8e78-ef10061fc57f,55,Other,Basic,24.58,18,Asia,Desktop,8.99,0,Debit Card,1,1.29,Documentary
b7c1bdad-cafb-4586-a15d-fc9ff30a8115,45,Female,Standard,7.39,6,Oceania,TV,13.99,0,PayPal,1,1.06,Romance
6e061f35-b1b5-4efe-9e37-f40a14d929b1,24,Male,Premium,6.92,13,Africa,Desktop,17.99,0,Crypto,2,0.49,Action
8c2d377b-f6ec-44b5-ae08-3660c4358a93,30,Other,Premium,1.37,55,North America,Mobile,17.99,1,Debit Card,1,0.02,Horror
afcc5c55-a3d8-4e2f-ab95-3d34f5e0390d,69,Female,Basic,24.56,53,Oceania,Laptop,8.99,1,Gift Card,1,0.45,Action
2211b077-0300-4e0c-834c-e7751a45eb96,47,Other,Standard,15.87,52,Africa,Laptop,13.99,1,Crypto,1,0.3,Sci-Fi
8d755725-4f16-4006-bdae-fa3dc9fa2579,49,Female,Standard,7.62,27,Asia,TV,13.99,0,Debit Card,3,0.27,Action
c39a5943-fe7c-46ec-8d3c-2a24ab46733b,67,Male,Standard,3.05,29,Oceania,Tablet,13.99,1,PayPal,1,0.1,Drama
e62d9bc8-dab9-42e0-b6b2-e8d076fe843b,23,Female,Premium,13.31,34,Africa,Mobile,17.99,1,Debit Card,2,0.38,Romance
c8648f0f-0b92-4445-a3a7-5c48711cbc07,57,Male,Premium,0.97,32,South America,Mobile,17.99,1,Gift Card,2,0.03,Comedy
ebe928a7-de65-4567-b349-06056b35e6a6,55,Other,Standard,21.58,48,North America,Mobile,13.99,0,Credit Card,5,0.44,Romance
8b3597af-7da9-405d-9815-60d1e4dbe2e5,35,Other,Standard,22.59,16,Europe,Tablet,13.99,0,Credit Card,2,1.33,Comedy
839ec473-5f41-4a8b-955a-ec14b3a9cad4,22,Female,Standard,9.69,35,Asia,TV,13.99,1,Crypto,4,0.27,Documentary
cdf4012d-14b0-41d5-ab40-cc6627fe1e3b,34,Male,Premium,12.82,45,North America,Mobile,17.99,1,PayPal,2,0.28,Romance
6ead42f9-86d8-4c66-b2fc-3d791323186d,25,Female,Premium,15.95,15,South America,Laptop,17.99,0,Credit Card,1,1,Action
9235d289-6d46-46ba-a48a-1cf4ea18b599,49,Other,Premium,2.05,14,North America,Tablet,17.99,0,Debit Card,5,0.14,Romance
20529e32-d3e7-4cfc-8210-b6468cdbe2a4,55,Other,Premium,3.86,25,Europe,Tablet,17.99,1,PayPal,3,0.15,Action
bfe7729e-7d5d-4850-b496-51e891158836,36,Other,Basic,1.68,10,Africa,TV,8.99,1,PayPal,4,0.15,Action
2117b36a-9e3e-4077-ac5b-03540bb38461,49,Male,Standard,4.22,50,Oceania,Desktop,13.99,1,Gift Card,2,0.08,Comedy
ceec2c10-9770-48d1-8366-344fa66195b1,54,Female,Basic,26.88,44,South America,Desktop,8.99,0,Gift Card,3,0.6,Drama
854b2bfd-6773-413f-b385-02338fa3a316,31,Female,Standard,2.23,39,North America,Mobile,13.99,1,Debit Card,5,0.06,Drama
ee53be31-fb36-41d9-8eb2-1a4c1d976552,31,Male,Premium,14.15,24,South America,Desktop,17.99,0,PayPal,5,0.57,Drama
022f9c7a-8276-494a-8629-086ad5e81df1,30,Male,Premium,8.79,21,Europe,Tablet,17.99,0,Crypto,4,0.4,Comedy
1a0f21b6-454a-4a22-88a8-5045b9d00fa4,58,Male,Standard,14.57,22,North America,Mobile,13.99,0,Debit Card,2,0.63,Romance
d1593b1d-ef59-4d4a-a169-5ff338b8baef,60,Male,Standard,3.01,30,Asia,Desktop,13.99,1,Gift Card,3,0.1,Documentary
749b69f5-8a24-428a-880c-86057af2a485,66,Male,Basic,12.05,33,South America,Tablet,8.99,1,PayPal,3,0.35,Drama
a2eab47c-dc4c-427f-88f8-755051b303fb,51,Female,Premium,3.7,37,South America,Mobile,17.99,1,Credit Card,2,0.1,Horror
b313f39d-0675-4bef-9b10-573146872adf,63,Male,Premium,5.84,20,Oceania,Mobile,17.99,0,Credit Card,1,0.28,Documentary
af9b0f0d-9532-48f2-ad24-bf41faa164a6,55,Other,Standard,2.89,37,North America,Desktop,13.99,1,Debit Card,4,0.08,Action
ec202012-e4bf-4b14-b5fe-4447d8cfb730,38,Male,Premium,29.84,56,South America,Desktop,17.99,0,Credit Card,4,0.52,Drama
8c78b61b-0d41-4470-ade0-3ed2e2b36c28,65,Other,Standard,19.33,31,North America,Desktop,13.99,0,Credit Card,1,0.6,Comedy
da57899f-77b4-4b23-bcab-700db438f6d1,43,Female,Premium,2.5,33,Europe,TV,17.99,1,Credit Card,3,0.07,Action
361aff57-8a5f-4229-b4f5-f52544178dc7,63,Male,Premium,6.97,31,North America,Tablet,17.99,1,Crypto,1,0.22,Romance
900034d1-e7de-4e99-914e-4ad863061834,64,Female,Standard,3.66,6,Africa,Mobile,13.99,0,PayPal,1,0.52,Romance
6082e011-4f6d-4acb-93f2-3bfefd532880,58,Female,Basic,30.85,46,North America,Mobile,8.99,0,Debit Card,5,0.66,Actionoading testsample.csv…]()




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
