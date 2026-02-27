# app.py

import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load("iris_model.pkl")

st.title("🌸 Iris Flower Classification App")

st.write("Enter flower details:")

# Input fields
sepal_length = st.number_input("Sepal Length", min_value=0.0)
sepal_width = st.number_input("Sepal Width", min_value=0.0)
petal_length = st.number_input("Petal Length", min_value=0.0)
petal_width = st.number_input("Petal Width", min_value=0.0)

# Prediction button
if st.button("Predict"):

    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

    prediction = model.predict(input_data)

    if prediction == 0:
        st.success("Prediction: Setosa")

    elif prediction == 1:
        st.success("Prediction: Versicolor")

    else:
        st.success("Prediction: Virginica")