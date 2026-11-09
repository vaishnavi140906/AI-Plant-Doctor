🌱 AI Plant Doctor

Deep Learning-Based Plant Disease Detection and Recommendation System

📌 Project Overview

AI Plant Doctor is a deep learning-based web application designed to detect plant diseases through leaf image analysis. Users can upload an image of a plant leaf, and the system predicts the possible disease using a trained TensorFlow/Keras model.

The application also provides disease information, confidence scores, estimated disease severity, plant health assessment, environmental risk analysis, and treatment and prevention recommendations.

The system aims to support early plant disease identification and help users make informed decisions about plant care.

🎯 Key Features

- Plant Disease Detection: Identifies plant diseases from uploaded leaf images using a trained deep learning model.
- Confidence Score: Displays the confidence level of the predicted disease.
- Disease Severity Estimation: Uses OpenCV-based image processing to estimate the affected leaf area.
- Plant Health Score: Provides an estimated health score out of 100.
- Environmental Risk Analysis: Evaluates disease risk using temperature, humidity, and rainfall inputs.
- Treatment Recommendations: Provides suggested treatments and preventive measures based on the predicted disease.
- Prediction History: Saves previous plant disease scans in a JSON file.
- User-Friendly Interface: Provides an interactive web interface for uploading images and viewing results.

🧠 Deep Learning Model

The project uses a trained image classification model developed using TensorFlow and Keras.

Model Details:

- Framework: TensorFlow / Keras
- Model File: "plant_model.keras"
- Input Image Size: 224 × 224 pixels
- Image Format: RGB
- Normalization: Pixel values divided by 255
- Classification: 38 plant disease classes

The model was trained using Google Colab. After training, the model was saved and integrated into the Flask application for prediction.

⚙️ Technologies Used

Category| Technologies
Programming Language| Python
Deep Learning| TensorFlow, Keras
Image Processing| OpenCV
Backend| Flask
Frontend| HTML, CSS, JavaScript
Data Processing| NumPy
Model Training| Google Colab
Development Environment| Visual Studio Code
Data Storage| JSON

🔄 System Workflow

1. The user opens the AI Plant Doctor web application.
2. The user uploads a plant leaf image.
3. The backend receives and preprocesses the image.
4. The image is resized to 224 × 224 pixels and normalized.
5. The trained deep learning model analyzes the image.
6. The system predicts the possible plant disease and confidence score.
7. OpenCV estimates the disease severity from the leaf image.
8. The system calculates a plant health score and environmental disease risk.
9. Treatment and prevention recommendations are displayed.
10. The prediction details are saved in the scan history.

📁 Project Structure

AI-Plant-Doctor/
│
├── app.py
├── app_backup.py
├── plant_model.keras
├── scan_history.json
├── .gitignore
│
├── static/
│   ├── style.css
│   └── script.js
│
└── templates/
    ├── index.html
    └── history.html

🚀 Installation and Execution

1. Install Dependencies

pip install flask tensorflow opencv-python numpy pillow

2. Run the Application

python app.py

3. Open in Browser

http://127.0.0.1:5000/

Upload a plant leaf image to detect possible diseases and view the recommendations.

🔮 Future Enhancements

- Support for additional plant species and diseases.
- Improved disease severity detection.
- Integration with real-time weather APIs.
- Mobile application development.
- More advanced treatment recommendations.
- Continuous model improvement using additional plant images.

📝 Conclusion

AI Plant Doctor demonstrates the application of deep learning and computer vision in agriculture. By combining image-based disease classification, severity estimation, environmental risk assessment, and treatment recommendations, the system provides an accessible approach to preliminary plant health monitoring.

The project highlights how Artificial Intelligence can contribute to smarter agricultural practices and support early plant disease management.
