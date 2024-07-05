import joblib
import os
import pandas as pd
from flask import Flask, request, jsonify

app = Flask(__name__)

def load_model(models_dir, model_name):
    try:
        model_filepath = os.path.join(models_dir, model_name)
        model = joblib.load(model_filepath)

        print("Model successfully loaded")
        return model
    except:
        print("Error loading model")


@app.route("/predict", methods=["POST"])
def predict():
    json_data = request.json

    input_data = pd.DataFrame(json_data, index=[0])

    prediction = model.predict(input_data)[0]

    json_response = {
        "Prediction" : prediction
    }

    return jsonify(json_response)

if __name__ == "__main__":
    model = load_model("models", "random_forest-v1.pkl")
    app.run(debug=True)
    