import streamlit as st
import pandas as pd
import joblib as jb
from preprocessing import preprocess

# Page Configuration
st.set_page_config(
    page_title="Credit Risk Prediction",
    page_icon="🏦",
    layout="wide"
)


# Load Model and Training Columns
model = jb.load(
    "models/credit_risk_model.pkl"
)

training_columns = jb.load(
    "models/training_columns.pkl"
)

# Title
st.title("🏦 Credit Risk Prediction System")
st.write(
    "Upload an Excel file containing customer details and predict the customer's credit risk category."
)


# File Upload
uploaded_file = st.file_uploader(
    "Choose an Excel file",
    type=["xlsx"]
)


# Prediction
if uploaded_file is not None:
    st.success("File uploaded successfully!")
    st.write("**Filename:**", uploaded_file.name)
    # Read uploaded Excel
    df_unseen = pd.read_excel(uploaded_file)
    st.subheader("Uploaded Data")
    st.dataframe(df_unseen)
    if st.button("Predict Credit Risk"):
        # Preprocess uploaded data
        df_encoded = preprocess(df_unseen)
        # Match training columns
        df_encoded = df_encoded.reindex(
            columns=training_columns,
            fill_value=0
        )

        # Predict
        predictions = model.predict(df_encoded)
        # Add prediction column
        df_unseen["Approved_Flag"] = predictions
        st.success("Prediction completed successfully!")
        st.subheader("Prediction Results")
        st.dataframe(df_unseen)

        # Convert dataframe to Excel
        from io import BytesIO
        output = BytesIO()
        with pd.ExcelWriter(output, engine="openpyxl") as writer:
            df_unseen.to_excel(writer, index=False)
        output.seek(0)
        st.download_button(
            label="📥 Download Prediction File",
            data=output,
            file_name="Final_Predictions.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )