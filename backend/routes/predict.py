from flask import Blueprint, request, jsonify
import pickle
import numpy as np

predict_bp = Blueprint("predict_bp", __name__)

# Load model
with open("models/BalBagging_multiclass.pkl", "rb") as file:
    model = pickle.load(file)

@predict_bp.route("/predict", methods=["GET", "POST"])
def predict():

    # GET request
    if request.method == "GET":

        return jsonify({
            "message": "Prediction API is running"
        })

    # Read JSON safely
    data = request.get_json(silent=True)

    # Check JSON exists
    if data is None:

        return jsonify({
            "error": "No JSON data received"
        }), 400

    # Check features key exists
    if "features" not in data:

        return jsonify({
            "error": "No features found"
        }), 400

    try:

        features = np.array(
            data["features"]
        ).reshape(1, -1)

        prediction = model.predict(features)
        
        
        if int(prediction[0]) == 0:
            result =" No Machine Failure"

        else:
            result = " Machine Failure"



        return jsonify({
            "prediction": result
        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500