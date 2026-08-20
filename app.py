from flask import Flask, render_template, request, jsonify
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np

app = Flask(__name__)

# Load trained AI model
model = load_model("plant_model.keras")

# IMPORTANT:
# Keep this in the EXACT same order as your dataset classes.
class_names = [
    "Apple___Apple_scab",
    "Apple___Black_rot",
    "Apple___Cedar_apple_rust",
    "Apple___healthy",
    "Blueberry___healthy",
    "Cherry_(including_sour)___Powdery_mildew",
    "Cherry_(including_sour)___healthy",
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot",
    "Corn_(maize)___Common_rust_",
    "Corn_(maize)___Northern_Leaf_Blight",
    "Corn_(maize)___healthy",
    "Grape___Black_rot",
    "Grape___Esca_(Black_Measles)",
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)",
    "Grape___healthy",
    "Orange___Haunglongbing_(Citrus_greening)",
    "Peach___Bacterial_spot",
    "Peach___healthy",
    "Pepper,_bell___Bacterial_spot",
    "Pepper,_bell___healthy",
    "Potato___Early_blight",
    "Potato___Late_blight",
    "Potato___healthy",
    "Raspberry___healthy",
    "Soybean___healthy",
    "Squash___Powdery_mildew",
    "Strawberry___Leaf_scorch",
    "Strawberry___healthy",
    "Tomato___Bacterial_spot",
    "Tomato___Early_blight",
    "Tomato___Late_blight",
    "Tomato___Leaf_Mold",
    "Tomato___Septoria_leaf_spot",
    "Tomato___Spider_mites Two-spotted_spider_mite",
    "Tomato___Target_Spot",
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus",
    "Tomato___Tomato_mosaic_virus",
    "Tomato___healthy"
]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    try:

        if "image" not in request.files:
            return jsonify({"error": "No image uploaded"}), 400

        file = request.files["image"]

        if file.filename == "":
            return jsonify({"error": "No image selected"}), 400

        # Open image
        image = Image.open(file).convert("RGB")
        image = image.resize((224, 224))

        # Prepare image
        image_array = np.array(image).astype("float32") / 255.0
        image_array = np.expand_dims(image_array, axis=0)

        # AI prediction
        prediction = model.predict(image_array, verbose=0)

        predicted_index = int(np.argmax(prediction))
        confidence = float(np.max(prediction)) * 100

        disease = class_names[predicted_index]

        # Separate plant and disease
        parts = disease.split("___")

        plant = parts[0].replace("_", " ")

        if len(parts) > 1:
            disease_name = parts[1].replace("_", " ")
        else:
            disease_name = "Unknown"

        # Recommendation
        if "healthy" in disease.lower():

            recommendation = (
                "Your plant appears healthy. "
                "Continue proper watering, sunlight and regular monitoring. 🌱"
            )

        elif "Late_blight" in disease:

            recommendation = (
                "Remove affected leaves, avoid watering the leaves directly, "
                "improve air circulation and monitor the plant regularly. 🍅"
            )

        elif "Early_blight" in disease:

            recommendation = (
                "Remove infected leaves, maintain good air circulation "
                "and avoid excess moisture on the foliage. 🌿"
            )

        elif "Powdery_mildew" in disease:

            recommendation = (
                "Improve air circulation, reduce excessive humidity "
                "and remove severely affected leaves. 🌱"
            )

        else:

            recommendation = (
                "Remove severely affected leaves and monitor the plant. "
                "Maintain proper watering, sunlight and air circulation. 🌿"
            )

        return jsonify({
            "prediction": disease_name,
            "plant": plant,
            "confidence": round(confidence, 2),
            "recommendation": recommendation,
            "message": "AI analysis completed successfully 🌿"
        })

    except Exception as e:

        print("Prediction Error:", e)

        return jsonify({
            "error": str(e)
        }), 500

if __name__ == "__main__":
    app.run(debug=True)