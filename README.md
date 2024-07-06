# HousingPH

Prediction of housing prices based on the following factors (i.e., features):
* Number of Bedrooms
* Number of Bathrooms
* Floor Area
* Land Area
* Urbanicity (i.e., Urban or Rural)

Dataset Source: https://www.kaggle.com/datasets/klekzee/phillipines-housing-market
Demo Link: https://housingph.streamlit.app/

# Data
* raw - contains the raw CSV file dataset
* interim - contains the CSV files for the intermediate versions of the dataset generated from the preprocessing steps or experiments
* processed - contains different versions of data splits (i.e., train, valid, test)

# Models
* Directory that contains all the models generated during experiments. Each model has its name and version number as the unique identifier. This is a must to keep track of the outputs of each experiment for comparison in case of improvements.
* Models are stored in serialized pickle (.pkl) files
* Model filename format: `{model_name}-{v#}.pkl`

# Notebooks
* Directory that contains notebook files of the experiments conducted which includes data wrangling, exploratory data analysis, model training, and model evaluation.
* Explore the notebooks to view the investigations conducted for the data and how model training and evaluation were performed.

# Source
* Directory that contains the following:
  *   API (`api.py`) - Purposely created for model deployment in web as applications communicate using this tool.
  *   Streamlit App (`st_app.py`) - Python code to demonstrate the deployment of the model.
 
# API Demonstration in Postman
![image](https://github.com/JerickoDG/HousingPH/assets/60811658/93fca76e-3f31-4d66-a71a-8e467bd2e8fb)

# Streamlit App Demo
![image](https://github.com/JerickoDG/HousingPH/assets/60811658/5ffc6c6b-a335-4187-991a-e807b00fe1da)

If you are interested in trying the Streamlit App locally, follow these steps:
1. Create a virtual environment and activate it.
2. Install all the dependecies from `requirements.txt` within the virtual environment
3. In the terminal, enter the command: `python source\st_app.py`. Open the Local URL provided.
   * Optional: In `st_app.py`, you may change "Local" to "API" in `generate_prediction()` if you wish to generate predictions using the `api.py`. However, run the `api.py` before doing so. It was set to "Local" since the API is not deployed online.
5. Provide your inputs and click submit to generate a prediction.
