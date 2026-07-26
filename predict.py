import pandas as pd
import joblib as jb
from preprocessing import preprocess

#load model
model = jb.load("models/credit_risk_model.pkl")
print("Model loaded successfully!")
#load columns
training_columns = jb.load(
    "models/training_columns.pkl"
)
print("Training columns loaded successfully!")
# Read unseen dataset
df_unseen = pd.read_excel(
    r"C:\ALL MTECH PROJECTS\MLETEproj\CreditIQ\Datasets\Unseen_Dataset.xlsx"
)

#preprocessing
df_encoded_unseen = preprocess(df_unseen)

print(df_encoded_unseen.head())

#matching columns

df_encoded_unseen = df_encoded_unseen.reindex(
    columns=training_columns,
    fill_value=0
)
print("Columns matched successfully!")

#predict

predictions = model.predict(df_encoded_unseen)
#Adding predictions to the original dataframe
df_unseen["Approved_Flag"] = predictions
# Save predictions to Excel
df_unseen.to_excel(
    r"C:\ALL MTECH PROJECTS\MLETEproj\CreditIQ\Final_Predictions.xlsx",
    index=False
)

print("Prediction file saved successfully!")