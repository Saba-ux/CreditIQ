#  CreditIQ – AI-Powered Credit Risk Assessment Platform

CreditIQ is an end-to-end Machine Learning application that predicts the credit risk category of loan applicants using financial and credit history data. The application enables users to upload customer information in Excel format, automatically preprocesses the data, predicts the customer's credit risk using a trained XGBoost model, and generates a downloadable prediction report through an interactive Streamlit web interface.

---

##  Live Demo

🔗 Live Application: https://creditiq-saba.streamlit.app

📂 GitHub Repository: https://github.com/Saba-ux/CreditIQ

---

##  Problem Statement

Financial institutions receive thousands of loan applications every day. Manually assessing each applicant's creditworthiness is time-consuming and can lead to inconsistent decisions.

CreditIQ automates this process by using Machine Learning to classify applicants into different credit risk categories based on their financial and credit history.

---

##  Features

- Upload customer datasets in Excel (.xlsx) format
- Automated data preprocessing
- Statistical feature selection
- Credit risk prediction using XGBoost
- Interactive Streamlit web application
- Download prediction results as an Excel file
- Modular and reusable project structure

---

##  Tech Stack

### Programming Language
- Python

### Machine Learning
- XGBoost
- Random Forest
- Decision Tree
- Scikit-learn

### Data Processing
- Pandas
- NumPy

### Statistical Analysis
- Chi-Square Test
- ANOVA
- Variance Inflation Factor (VIF)

### Deployment
- Streamlit

### Model Serialization
- Joblib

---

##  Machine Learning Workflow

1. Data Collection
2. Data Cleaning
3. Feature Selection
4. Data Encoding
5. Model Training
6. Hyperparameter Tuning
7. Model Evaluation
8. Model Serialization
9. Deployment using Streamlit

---

##  Feature Selection Techniques

The following statistical techniques were used to select relevant features:

- Chi-Square Test (Categorical Features)
- Variance Inflation Factor (VIF)
- ANOVA Test (Numerical Features)

---

##  Models Evaluated

The following classification models were trained and compared:

- Decision Tree
- Random Forest
- XGBoost

After comparing the evaluation metrics, XGBoost produced the best overall performance and was selected as the final model.

---

##  Evaluation Metrics

The models were evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score

These metrics were calculated for each credit risk category to ensure balanced model performance.

---


##  Application Workflow

1. Upload an Excel file containing customer information.
2. The application preprocesses the uploaded data.
3. Features are aligned with the trained model.
4. XGBoost predicts the credit risk category.
5. Results are displayed in the web application.
6. Users can download the prediction report as an Excel file.

---

##  Screenshots

### Home Page

<img width="1466" height="827" alt="Screenshot 2026-08-05 at 1 26 52 AM" src="https://github.com/user-attachments/assets/71eec105-5dd5-4bd1-8e8f-6a601117c548" />


---

### Prediction Results

(Add screenshot here)

---

##  Future Improvements

- Integration with real banking APIs
- Explainable AI using SHAP values
- Probability-based risk scoring
- User authentication
- Database integration
- REST API using FastAPI
- Docker deployment
- Cloud deployment on AWS/Azure/GCP

---

## 👨‍💻 Author

**Saba**

M.Tech (Data Science)

Delhi Technological University

GitHub: https://github.com/Saba-ux
