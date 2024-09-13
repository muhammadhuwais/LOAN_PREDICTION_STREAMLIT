import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open(r'model.pkl', 'rb') as file:
    model = pickle.load(file)

# Define a function for prediction
def predict_loan_status(inputs):
    """Predict loan approval status based on user inputs."""
    inputs = np.array(inputs).reshape(1, -1)  # Reshape input for prediction
    prediction = model.predict(inputs)
    return prediction[0]

# Streamlit app
def main():
    """Main function to run the Loan Prediction App."""
    
    # Setting up the page layout
    st.set_page_config(page_title="Loan Prediction App", layout="wide")
    
    # Title and description
    st.markdown("<h1 style='text-align: center; color: #4CAF50;'>Loan Prediction App</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #808080;'>Fill in the details below to predict your loan approval status</h3>", unsafe_allow_html=True)
    st.write("---")
    
    # Create columns for a clean layout
    col1, col2 = st.columns(2)

    with col1:
        loan_id = st.text_input("Loan ID")
        gender = st.selectbox("Gender", ["Male", "Female"])
        married = st.selectbox("Marital Status", ["Yes", "No"])
        dependents = st.selectbox("Number of Dependents", ["0", "1", "2", "3+"])
        education = st.selectbox("Education Level", ["Graduate", "Not Graduate"])

    with col2:
        self_employed = st.selectbox("Self Employed?", ["Yes", "No"])
        applicant_income = st.number_input("Applicant Income", min_value=0, step=100)
        coapplicant_income = st.number_input("Coapplicant Income", min_value=0, step=100)
        loan_amount = st.number_input("Loan Amount (in thousands)", min_value=0, step=1)
        loan_amount_term = st.number_input("Loan Amount Term (in months)", min_value=0, step=1)
        credit_history = st.selectbox("Credit History", ["0", "1"])
        property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

    # Spacing for better UI
    st.write(" ")
    
    # Predict button
    if st.button("Predict Loan Status"):
        # Convert inputs to numeric values
        gender = 1 if gender == "Male" else 0
        married = 1 if married == "Yes" else 0
        dependents = {"0": 0, "1": 1, "2": 2, "3+": 3}[dependents]
        education = 1 if education == "Graduate" else 0
        self_employed = 1 if self_employed == "Yes" else 0
        property_area = {"Urban": 0, "Semiurban": 1, "Rural": 2}[property_area]

        # Prepare input for prediction
        inputs = [
            gender, married, dependents, education, self_employed,
            applicant_income, coapplicant_income, loan_amount, loan_amount_term,
            credit_history, property_area
        ]

        # Make prediction
        result = predict_loan_status(inputs)

        # Display result
        if result == 1:
            st.success("🎉 Congratulations! Your loan is approved.")
        else:
            st.error("🚫 Sorry, your loan is not approved.")
    
    # Footer
    st.write("---")
    st.markdown("<p style='text-align: center; color: #808080;'>Developed with ❤️ by [uwais]</p>", unsafe_allow_html=True)

if __name__ == '__main__':
    main()
