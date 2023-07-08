from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import pickle
import sklearn
import pandas as pd


"""{
  "sample": "bone_marrow",
  "fluid": "HCl",
  "percentage": 12.5,
  "day": 5,
  "month": 5,
  "year": 2023
}"""

# Create a dictionary for mapping
mapping = {
    'HCl': 0,
    'EDTA': 1,
    'gooding_and_stewart': 2,
    'formic_acid': 3,
    'hammersmith': 4,
    'nitric_acid': 5,
    'edta': 6,
    'trichloroacetic_acid': 7,
    'formalin_nitric': 8
}
# Create a dictionary for mapping
mapping2 = {
    'bone_marrow': 0,
    'premolar_tooth': 1,
    'molar_tooth': 2,
    'incisor_tooth': 3,
    'canine_tooth': 4
}




app = Flask(__name__)
cors = CORS(app) #Allow Cross Origin
app.config['CORS_HEADERS'] = 'Content-Type'

# Load the pickled model
with open('decision_tree_model.pkl', 'rb') as file:
    model = pickle.load(file,encoding= "ASCII")


@app.route('/')
@cross_origin()
def index():
    return("Welcome, please smile more")

@app.route('/predict', methods=['POST'])
@cross_origin()
def predict():
    # Retrieve the JSON payload from the request
    data = request.get_json()

    # Convert the JSON data into a DataFrame
    features = pd.DataFrame(data, index=[0])
        # Map the values in the "sample" column
    features["sample"] = features["sample"].map(mapping2)

    # Map the values in the "fluid" column
    features["fluid"] = features["fluid"].map(mapping)

    # Make predictions using the loaded model
    prediction = model.predict(features)

    # Prepare the response as JSON
    response = {'prediction': prediction[0]}

    return jsonify(response)

if __name__ == '__main__':
    app.run()
