import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open(r'model.pkl', 'rb') as file:
    model = pickle.load(file)

# Define a function for prediction
def predict_loan_status(inputs):
    # Convert input to numpy array and reshape for model
    inputs = np.array(inputs).reshape(1, -1)
    prediction = model.predict(inputs)
    return prediction[0]

# Streamlit app
def main():
    st.title("Loan Prediction App")

    # Collect user input
    loan_id = st.text_input("Loan ID")
    gender = st.selectbox("Gender", ("Male", "Female"))
    married = st.selectbox("Married", ("Yes", "No"))
    dependents = st.selectbox("Dependents", ("0", "1", "2", "3+"))
    education = st.selectbox("Education", ("Graduate", "Not Graduate"))
    self_employed = st.selectbox("Self Employed", ("Yes", "No"))
    applicant_income = st.number_input("Applicant Income", min_value=0)
    coapplicant_income = st.number_input("Coapplicant Income", min_value=0)
    loan_amount = st.number_input("Loan Amount (in thousands)", min_value=0)
    loan_amount_term = st.number_input("Loan Amount Term (in months)", min_value=0)
    credit_history = st.selectbox("Credit History", ("0", "1"))
    property_area = st.selectbox("Property Area", ("Urban", "Semiurban", "Rural"))
    
    # Process inputs
    if st.button("Predict"):
        inputs = [gender, married, dependents, education, self_employed,
                  applicant_income, coapplicant_income, loan_amount, loan_amount_term,
                  credit_history, property_area]
        
        # Map categorical inputs to numeric values (you need to match your preprocessing)
        gender = 1 if gender == "Male" else 0
        married = 1 if married == "Yes" else 0
        dependents = 0 if dependents == "0" else (1 if dependents == "1" else (2 if dependents == "2" else 3))
        education = 1 if education == "Graduate" else 0
        self_employed = 1 if self_employed == "Yes" else 0
        property_area = 0 if property_area == "Urban" else (1 if property_area == "Semiurban" else 2)
        
        # Prepare final input array
        final_input = [gender, married, dependents, education, self_employed,
                       applicant_income, coapplicant_income, loan_amount, loan_amount_term,
                       credit_history, property_area]
        
        result = predict_loan_status(final_input)
        if result == 1:
            st.success("Loan Approved")
        else:
            st.error("Loan Not Approved")

if __name__ == '__main__':
    main()
