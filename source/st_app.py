import streamlit as st
from inference import generate_prediction

st.title("Housing Price Predictor")
st.image("https://etc.usf.edu/clipart/22100/22188/modernhouse_22188_lg.gif")

# Input section
num_bedrooms = st.number_input("Number of Bedrooms", min_value=1)
num_bathrooms = st.number_input("Number of Bathrooms", min_value=1)
floor_area = st.number_input("Floor Area", min_value=1.00)
land_area = st.number_input("Land Area", min_value=1.00)
urbanicity = st.selectbox("Urbanicity", ["Urban", "Rural"])

submitted = st.button("Submit")

# If submit button is clicked, generate prediction
if submitted:
    data = {
        "Bedrooms" : num_bedrooms,
        "Bathrooms" : num_bathrooms,
        "Floor Area" : floor_area,
        "Land Area" : land_area,
        "Urbanicity" : urbanicity
    }

    prediction = generate_prediction(data, "Local")
    if prediction == None:
        st.code("No prediction generated. Only Local or API argument values are accepted on the source parameter of generate_prediction()")
    else:
        st.code(f"Prediction: {prediction}")