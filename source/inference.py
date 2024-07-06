import requests
import os
import joblib
import pandas as pd

"""
Function to load the model
models_dir - string that represents the directory where the model file is located
model_filename - filename of the model
"""
def load_model(models_dir, model_filename):
    try:
        model_filepath = os.path.join(models_dir, model_filename)
        model = joblib.load(model_filepath)

        print("Model successfully loaded")
        return model
    except:
        print("Error loading model")

"""
Function to generate a prediction
Accepts input_data in a dictionary format
Source:
    API - Uses the endpoint from the Flask API to generate predictions. Run the `api.py` to use this.
    Local - Does not use the Flask API. Generates prediction locally.
"""
def generate_prediction(input_data, source):
    sources = ["Local", "API"]

    if source in sources:
        if source == "API":
            url_endpoint = "http://127.0.0.1:5000/predict"
            response = requests.post(url=url_endpoint, json=input_data)

            if response.status_code == 200:
                response_data = response.json()
                prediction = response_data["Prediction"]
                return prediction
            else:
                print("Error:", response.status_code, response.text)
                return None
        
        elif source == "Local":
            model = load_model("models", "random_forest-v1.pkl")
            prediction = model.predict(pd.DataFrame(input_data, index=[0]))[0]

            return prediction
        
        else:
            print("Source can only be [API or Local]")
            return None
    else:
        print("Source can only be [API or Local]")
        return None
