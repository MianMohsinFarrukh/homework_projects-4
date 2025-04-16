import streamlit as st
import pandas as pd

st.title("BMI Calculator")
height = st.slider('Enter your height (cm)', 100, 250, 175)
weight = st.slider('Enter your weight (kg)', 40, 200, 70)

bmi = weight / ((height / 100) ** 2)
st.write(f"Your BMI is: {bmi:.2f}")
st.write("### BMI Categories: ###")
st.write(" - Underweight: < 18.5")
st.write(" - Normal weight: 18.5–24.9")
st.write(" - Overweight: 25–29.9")
st.write(" - Obesity: BMI ≥ 30")
