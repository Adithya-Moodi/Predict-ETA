import streamlit as st
import joblib
import pandas as pd

# Load the trained model
model = joblib.load("xgb_model.pkl")

# Load mapping file
mapping_file = "mapping_file.xlsx"
mapping_df = pd.read_excel(mapping_file, sheet_name="Sheet1")

st.title("XGBoost Prediction App")

st.write("Enter the input features below:")

# --- Distance input ---
distance_km = st.number_input("Distance (km)", min_value=0.0, step=0.1)

# --- Seller selection ---
seller_id = st.selectbox("Select Seller ID", mapping_df["seller_id"].unique())
seller_row = mapping_df[mapping_df["seller_id"] == seller_id].iloc[0]
seller_city = seller_row["seller_city"]
seller_state = seller_row["seller_state"]

st.write(f"📍 Seller City: **{seller_city}**, Seller State: **{seller_state}**")

# --- Customer selection ---
customer_city = st.selectbox("Select Customer City", mapping_df["customer_city"].unique())
customer_row = mapping_df[mapping_df["customer_city"] == customer_city].iloc[0]
customer_state = customer_row["customer_state"]

st.write(f"🏠 Customer State: **{customer_state}**")

# --- Predict button ---
if st.button("Predict"):
    # Build input DataFrame
    input_data = pd.DataFrame([[
        distance_km,
        customer_state,
        seller_city,
        customer_city,
        seller_id,
        seller_state
    ]], columns=[
        "distance_km",
        "customer_state",
        "seller_city",
        "customer_city",
        "seller_id",
        "seller_state"
    ])
    
    # Convert categorical columns to category dtype
    categorical_cols = ["customer_state", "seller_city", "customer_city", "seller_id", "seller_state"]
    for col in categorical_cols:
        input_data[col] = input_data[col].astype("category")
    
    # Make prediction
    prediction = model.predict(input_data)
    hours = round(prediction[0])  # round to nearest hour
    days = hours // 24
    rem_hours = hours % 24
    
    # Format result
    formatted_output = f"{days} Days {rem_hours} Hours"
    
    st.success(f"Predicted value: {formatted_output}")