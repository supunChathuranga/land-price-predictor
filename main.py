from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the Land Price Predictor!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    distance = data.get("distance", 0)
    school_distance = data.get("school_distance", 0)

    # Simple price prediction logic
    price = 6_000_000 - (distance * 200_000) - (school_distance * 100_000)
    return jsonify({"predicted_price": f"Rs {price:,.2f}"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
