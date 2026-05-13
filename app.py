import streamlit as st
import joblib
import pandas as pd
import os

st.title("Fraud Detection System")
st.write("Enter transaction details to check for fraud.")

# Load model from the same folder as app.p
model_path = os.path.join(os.path.dirname(__file__), "fraud_model.pkl")
model = joblib.load(model_path)

amount = st.number_input("Transaction Amount ($)", min_value=0)
txn_type = st.selectbox("Transaction Type", ["Payment", "Transfer", "Cash Out"])
old_balance = st.number_input("Old Balance ($)", min_value=0)
new_balance = st.number_input("New Balance ($)", min_value=0)

if st.button("Check Transaction"):
    if amount > 100000 and new_balance == 0:
        st.error("🚨 FRAUD DETECTED!")
    else:
        st.success("✅ Transaction is Safe")