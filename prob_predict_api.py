import pickle
from flask import Flask, request, jsonify
from flasgger import Swagger
import numpy as np
import pandas as pd

with open('logreg.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/predict_file', methods=["POST"])
def predict_manufacturer_probability():
    """calculate the probability that a car is made by one of thetop 25 manufacturers
    ---
    parameters:
      - name: input_file
        in: formData
        type: file
        required: true
    """
    input_data = pd.read_csv(request.files.get("input_file"), header=None)
	input_data_processed= preprocess_pipeline.fit_transform(input_data)
    prediction = model.predict_proba(input_data_processed)
    return str(list(prediction))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 