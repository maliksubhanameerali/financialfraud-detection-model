import streamlit as st
import pandas as pd
import joblib

model = joblib.load("fraud_detection_pipeline.pkl")

st.title("Fraud Detection Prediction App")

st.markdown("Please enter the transactional details to predict whether a transaction is fraudulent or not:")

st.divider()

transaction_type = st.selectbox("Transaction Type", ["CASH_OUT", "PAYMENT", "CASH_IN", "TRANSFER", "DEPOSIT"])
amount = st.number_input("Amount", min_value=0.0, value = 1000.0)
oldbalanceoriginal = st.number_input("Old Balance Original (Sender)", min_value=0.0, value = 10000.0)
newbalanceoriginal = st.number_input("New Balance Original (Sender)", min_value=0.0, value = 9000.0)
oldbalancedest = st.number_input("Old Balance Destination(Receiver)", min_value=0.0, value = 0.0)
newbalancedest = st.number_input("New Balance Destination(Receiver)", min_value=0.0, value = 0.0)

if st.button("Predict"):
    input_data = pd.DataFrame([{
        "type": transaction_type,
        "amount": amount,
        "oldbalanceOrg": oldbalanceoriginal,
        "newbalanceOrig": newbalanceoriginal,
        "oldbalanceDest": oldbalancedest,
        "newbalanceDest": newbalancedest
    }])

    prediction = model.predict(input_data)[0]
    st.subheader(f"Prediction Result: '{int(prediction)}'")

    if prediction == 1:
        st.error("The transaction is predicted to be FRAUDULENT.")
    else:
        st.success("The transaction is predicted to be LEGITIMATE.")