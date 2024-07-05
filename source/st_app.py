import streamlit as st
import requests

st.title("Housing Price Predictor")
st.image("https://etc.usf.edu/clipart/22100/22188/modernhouse_22188_lg.gif")

num_bedrooms = st.number_input("Number of Bedrooms", min_value=1)
num_bathrooms = st.number_input("Number of Bathrooms", min_value=1)
floor_area = st.number_input("Floor Area", min_value=1.00)
land_area = st.number_input("Land Area", min_value=1.00)
urbanicity = st.selectbox("Urbanicity", ["Urban", "Rural"])

submitted = st.button("Submit")

if submitted:
    data = {
        "Bedrooms" : num_bedrooms,
        "Bathrooms" : num_bathrooms,
        "Floor Area" : floor_area,
        "Land Area" : land_area,
        "Urbanicity" : urbanicity
    }

    url_endpoint = "http://127.0.0.1:5000/predict"

    response = requests.post(url=url_endpoint, json=data)

    if response.status_code == 200:
        response_data = response.json()
        prediction = response_data["Prediction"]
        st.code(f"Prediction: {prediction}")
    else:
        print("Error:", response.status_code, response.text)