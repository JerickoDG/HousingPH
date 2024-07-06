import joblib
import os
import pandas as pd
from flask import Flask, request, jsonify
from inference import load_model

app = Flask(__name__)

# Endpoint for model inference (prediction) - POST method only
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get data from body
        json_data = request.json
        input_data = pd.DataFrame(json_data, index=[0])

        # Generate prediction
        prediction = model.predict(input_data)[0]

        # Create a json_response dict
        json_response = {
            "Prediction" : prediction
        }

        # Return a JSON object
        return jsonify(json_response)
    
    except Exception as e:
        # Return the error if there is/are
        return jsonify({"error" : f"{e}"})
        

if __name__ == "__main__":
    model = load_model("models", "random_forest-v1.pkl") # Load the model once the API is started
    app.run(debug=True)
    