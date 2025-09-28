import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler
import plotly.express as px
import plotly.graph_objects as go

# Set page config for better layout
st.set_page_config(page_title="OTT Churn Prediction Dashboard", page_icon="📊", layout="wide")

# Load model and scaler
try:
    model = joblib.load('xgb_model.pkl')
    scaler = joblib.load('scaler.pkl')
    st.success("Model and scaler loaded successfully.")
except Exception as e:
    st.error(f"Failed to load model/scaler: {e}")
    st.stop()

# Expected columns (without 'churned')
expected_columns = [
    'customer_id', 'age', 'gender', 'subscription_type', 'watch_hours',
    'last_login_days', 'region', 'device', 'monthly_fee', 'payment_method',
    'number_of_profiles', 'avg_watch_time_per_day', 'favorite_genre'
]

# Preprocess function
def preprocess_data(df):
    try:
        df = df.copy()
        if 'customer_id' in df.columns:
            df = df.drop(['customer_id'], axis=1)
        if 'churned' in df.columns:
            df = df.drop(['churned'], axis=1)
        
        # Check columns
        missing_cols = [col for col in expected_columns[1:] if col not in df.columns]
        if missing_cols:
            raise ValueError(f"Missing columns: {missing_cols}")
        
        # Check for missing values
        if df.isnull().any().any():
            raise ValueError("CSV contains missing values.")
        
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
    except Exception as e:
        st.error(f"Preprocessing error: {e}")
        return None

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

# Sidebar for navigation and filters
st.sidebar.title("Dashboard Controls")
st.sidebar.markdown("Adjust filters and settings below:")
risk_filter = st.sidebar.selectbox("Filter by Risk Level", ["All", "High", "Low"])
subscription_filter = st.sidebar.multiselect("Filter by Subscription Type", ["Basic", "Standard", "Premium"], default=["Basic", "Standard", "Premium"])
region_filter = st.sidebar.multiselect("Filter by Region", ["Africa", "Asia", "Europe", "North America", "South America", "Oceania"], default=["Africa", "Asia", "Europe", "North America", "South America", "Oceania"])

# Main UI
st.title('📊 OTT Churn Prediction Dashboard')
st.markdown("Upload a subscriber CSV file to predict churn probabilities and view insights.")
st.markdown(f"**Expected columns**: {', '.join(expected_columns)}")

# File uploader
uploaded_file = st.file_uploader('Choose a CSV file', type='csv')
if uploaded_file is not None:
    with st.spinner("Processing your file..."):
        try:
            # Read CSV
            df = pd.read_csv(uploaded_file)
            original_df = df.copy()
            
            # Preprocess
            X = preprocess_data(df)
            if X is None:
                st.error("Failed to preprocess data. See error above.")
                st.stop()
            
            # Predict
            probs = model.predict_proba(X)[:, 1]
            original_df['churn_probability'] = probs.round(3)  # Round for display
            original_df['risk_level'] = original_df['churn_probability'].apply(lambda p: 'High' if p > 0.6 else 'Low')
            original_df['recommended_action'] = original_df.apply(lambda row: get_action(row['churn_probability'], row), axis=1)

            # Apply filters
            filtered_df = original_df
            if risk_filter != "All":
                filtered_df = filtered_df[filtered_df['risk_level'] == risk_filter]
            if subscription_filter:
                filtered_df = filtered_df[filtered_df['subscription_type'].isin(subscription_filter)]
            if region_filter:
                filtered_df = filtered_df[filtered_df['region'].isin(region_filter)]

            # Summary metrics in cards
            st.subheader("📈 Churn Risk Summary")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Total Subscribers", len(original_df))
            with col2:
                at_risk = original_df[original_df['churn_probability'] > 0.6]
                st.metric("At-Risk Subscribers (>0.6)", len(at_risk))
            with col3:
                st.metric("Percentage At-Risk", f"{len(at_risk)/len(original_df)*100:.2f}%")

            # Visualizations
            st.subheader("📊 Churn Probability Distribution")
            fig = px.histogram(original_df, x='churn_probability', nbins=30, title="Distribution of Churn Probabilities",
                              color_discrete_sequence=['#1f77b4'])
            st.plotly_chart(fig, use_container_width=True)

            st.subheader("📊 Churn Risk by Subscription Type")
            risk_by_sub = original_df.groupby('subscription_type')['churn_probability'].mean().reset_index()
            fig_sub = px.bar(risk_by_sub, x='subscription_type', y='churn_probability', title="Average Churn Probability by Subscription Type",
                            color='subscription_type', color_discrete_sequence=['#1f77b4', '#ff7f0e', '#2ca02c'])
            st.plotly_chart(fig_sub, use_container_width=True)

            # Display filtered subscribers with pagination
            st.header('All Subscribers')
            page_size = 50
            page_number = st.number_input("Page Number", min_value=1, value=1, step=1)
            start_idx = (page_number - 1) * page_size
            end_idx = start_idx + page_size
            st.dataframe(
                filtered_df.iloc[start_idx:end_idx].style.apply(
                    lambda x: ['background: salmon' if x['risk_level'] == 'High' else 'background: lightgreen' for _ in x],
                    axis=1
                ).format({'churn_probability': '{:.3f}'}),  # Format probability
                height=400,
                use_container_width=True
            )

            # Display at-risk users
            st.header('At-Risk Users (Probability > 0.6)')
            at_risk_filtered = filtered_df[filtered_df['churn_probability'] > 0.6]
            if not at_risk_filtered.empty:
                st.dataframe(
                    at_risk_filtered.style.apply(
                        lambda x: ['background: salmon' for _ in x], axis=1
                    ).format({'churn_probability': '{:.3f}'}), 
                    height=200,
                    use_container_width=True
                )
            else:
                st.write("No at-risk users found after filtering.")

            # Download options
            st.subheader("💾 Export Results")
            col1, col2 = st.columns(2)
            with col1:
                st.download_button(
                    label="Download Predictions as CSV",
                    data=original_df.to_csv(index=False),
                    file_name="churn_predictions.csv",
                    mime="text/csv"
                )
            with col2:
                st.download_button(
                    label="Download Predictions as JSON",
                    data=original_df.to_json(orient='records', lines=True),
                    file_name="churn_predictions.json",
                    mime="application/json"
                )
        except Exception as e:
            st.error(f"Error processing file: {e}")