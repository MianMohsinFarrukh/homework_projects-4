import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import joblib

st.title("Welcome to My Streamlit App!")
st.write("This is a demo application.")


data = {
    'Name': ['John', 'Jane', 'Alice', 'Bob'],
    'Age': [28, 34, 29, 42],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}   
df = pd.DataFrame(data)

city = st.selectbox("Select a city", df['City'].unique())
filtered_df = df[df['City'] == city]

st.write(f"Data for {city}:")
st.dataframe(filtered_df)


data = pd.DataFrame(
    np.random.randn(100, 3),
    columns=['x', 'y','z']
)
st.title("Line_Chart")
st.line_chart(data)
st.title("Bar_Chart")
st.bar_chart(data)





st.title("plotly_chart")
fruit = ({
    "fruits": ["apple", "banana", "orange", "mango"],
    "quantity": [10, 20, 15, 5]
})
fig = px.bar(fruit, x="fruits", y="quantity")
st.plotly_chart(fig)




st.title("Model Prediction")
model = joblib.load("liner_regression_model.pkl")

st.title("Model Prediction")
st.write("This is a demo application for model prediction.")

feature_value =st.number_input("Enter a feature value:", min_value=0, max_value=100, value=2)

if st.button('Predict'):
   prediction = model.predict([[feature_value]])[0][0]
   st.write(f"Prediction: {prediction:.2f}")