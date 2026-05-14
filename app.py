import streamlit as st
import joblib
import pandas as pd
import numpy as np

st.title("Fraud Detection System")
st.write("Enter transaction details to check for fraud.")

# Load model
model = joblib.load("fraud_model.pkl")

# Default mean values for V1-V28 (replace with your actual means)
default_means = {
    'V1': 0.0, 'V2': 0.0, 'V3': 0.0, 'V4': 0.0, 'V5': 0.0,
    'V6': 0.0, 'V7': 0.0, 'V8': 0.0, 'V9': 0.0, 'V10': 0.0,
    'V11': 0.0, 'V12': 0.0, 'V13': 0.0, 'V14': 0.0, 'V15': 0.0,
    'V16': 0.0, 'V17': 0.0, 'V18': 0.0, 'V19': 0.0, 'V20': 0.0,
    'V21': 0.0, 'V22': 0.0, 'V23': 0.0, 'V24': 0.0, 'V25': 0.0,
    'V26': 0.0, 'V27': 0.0, 'V28': 0.0
}

# Ask if user has PCA data
has_pca = st.radio(
    "Do you have PCA features (V1-V28)?",
    ["No, use default values", "Yes, I'll enter them"]
)

st.subheader("Basic Information")
time = st.number_input("Time (seconds since first transaction)", min_value=0.0)
amount = st.number_input("Transaction Amount ($)", min_value=0.0)

# Build feature dictionary
features = {'Time': time, 'Amount': amount}

if has_pca == "Yes, I'll enter them":
    st.subheader("PCA Features (V1-V28)")
    for i in range(1, 29):
        features[f'V{i}'] = st.number_input(f'V{i}', value=0.0)
else:
    # Use default means
    for i in range(1, 29):
        features[f'V{i}'] = default_means[f'V{i}']

if st.button("Check Transaction"):
    # Create DataFrame with all 30 features in correct order
    cols = ['Time'] + [f'V{i}' for i in range(1, 29)] + ['Amount']
    transaction = pd.DataFrame([features])[cols]
    
    # Model predicts
    prediction = model.predict(transaction)[0]
    
    if prediction == 1:
        st.error(" FRAUD DETECTED!")
        st.write("This transaction has been flagged as fraudulent.")
    else:
        st.success(" Transaction is Safe")
        st.write("No fraud detected.")
