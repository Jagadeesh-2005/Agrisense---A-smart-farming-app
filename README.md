# 🌾 AgriSense: Intelligent Crop Recommendation and Disease Detection System

## 📖 Overview

AgriSense is an AI-powered smart farming application designed to assist farmers in making better agricultural decisions. The system integrates Machine Learning, Deep Learning, Weather Monitoring, and Fertilizer Recommendation to provide intelligent support for crop cultivation.

The application recommends suitable crops based on soil and environmental conditions, detects plant diseases from leaf images, suggests fertilizers, provides farming recommendations, and displays weather information to support sustainable agriculture.

---

## 🎯 Project Objectives

* Recommend the most suitable crop based on soil nutrients and climatic conditions.
* Detect plant diseases from leaf images using Deep Learning.
* Provide fertilizer recommendations based on soil and crop characteristics.
* Offer farming suggestions and precautionary measures.
* Display real-time weather information to assist farming decisions.
* Promote smart and sustainable agriculture through Artificial Intelligence.



## 🚀 Key Features

### 🌾 Crop Recommendation

* Predicts the best crop for cultivation.
* Uses soil parameters:

  * Nitrogen (N)
  * Phosphorus (P)
  * Potassium (K)
  * Temperature
  * Humidity
  * pH Value
  * Rainfall

### 🦠 Disease Detection

* Upload crop leaf images.
* Detect plant diseases using a Convolutional Neural Network (CNN).
* Supports image-based diagnosis.

### 🧪 Fertilizer Recommendation

* Suggests suitable fertilizers based on:

  * Soil type
  * Crop type
  * Moisture
  * Nutrient levels

### 🌱 Farming Suggestions

* Provides crop-specific cultivation guidance.
* Helps farmers improve productivity and yield.

### ⚠️ Precautions

* Displays preventive measures for crop protection.
* Helps reduce disease and pest attacks.

### 🌦 Weather Report

* Provides real-time weather information.
* Displays:

  * Temperature
  * Humidity
  * Wind Speed
  * Weather Conditions

---

## 🏗️ System Architecture

```text
User
   │
   ▼
Streamlit Frontend
   │
   ├── Crop Recommendation Model
   ├── Disease Detection Model
   ├── Fertilizer Recommendation Model
   ├── Weather API
   └── AI-Based Suggestions Module
```

---

## 🛠️ Technologies Used

### Programming Language

* Python

### Frontend

* Streamlit

### Machine Learning

* Scikit-Learn
* Random Forest

### Deep Learning

* TensorFlow
* Keras
* CNN

### Image Processing

* OpenCV
* Pillow (PIL)

### Data Processing

* NumPy
* Pandas

### APIs

* OpenWeatherMap API
* OpenAI API (Optional)

### Version Control

* Git
* GitHub

---

## 📂 Project Structure

```text
AgriSense/
│
├── app.py
├── utils.py
│
├── crop_recommendation.py
├── disease_detection.py
├── fertilizer_recommendation.py
├── suggestions.py
├── weather_report.py
│
├── RF.pkl
├── disease_model.keras
├── fertilizer_model.pkl
│
├── soil_encoder.pkl
├── crop_encoder.pkl
├── fertilizer_encoder.pkl
│
├── disease_classes.txt
│
├── crop_images/
│
├── images/
│   ├── welcome_bg.jpeg
│   ├── dashboard_bg.jpg
│   ├── crop_bg.jpg
│   ├── disease_bg.jpg
│   ├── fertilizer_bg.jpg
│   ├── suggestion_bg.jpg
│   └── precaution_bg.jpg
│
└── requirements.txt
```

---

## 📊 Machine Learning Models

### Crop Recommendation Model

* Algorithm: Random Forest Classifier
* Output: Recommended Crop

### Disease Detection Model

* Algorithm: Convolutional Neural Network (CNN)
* Input: Leaf Image
* Output: Disease Prediction

### Fertilizer Recommendation Model

* Algorithm: Machine Learning Classification Model
* Output: Recommended Fertilizer

---

## ▶️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/agrisense.git
cd agrisense
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

## 📸 Application Modules

### Welcome Page

Modern agriculture-themed landing page.

### Dashboard

Central navigation hub for all services.

### Crop Recommendation

Predicts suitable crops using soil and climate data.

### Disease Detection

Identifies crop diseases from uploaded leaf images.

### Fertilizer Recommendation

Suggests fertilizers based on crop and soil conditions.

### Suggestions & Precautions

Provides farming guidance and preventive measures.

### Weather Report

Displays current weather conditions.

---

## 🔮 Future Enhancements

* AI Chatbot for Farmers
* Voice-Based Assistance
* Multi-Language Support
* GPS-Based Farm Monitoring
* Satellite Crop Monitoring
* Market Price Prediction
* Mobile Application Deployment
* IoT Sensor Integration


## 📜 License

This project is developed for educational and research purposes.

---

## ⭐ Acknowledgements

* TensorFlow
* Scikit-Learn
* Streamlit
* OpenWeatherMap
* OpenAI
* Open Source Agriculture Datasets

---

### 🌱 Smart Farming Through Artificial Intelligence

### 🚜 Empowering Farmers with Data-Driven Decisions





**OUTPUT**
<img width="1920" height="1020" alt="Screenshot 2026-06-17 112632" src="https://github.com/user-attachments/assets/c00d2e5f-aacf-4662-841d-4f22f52c84a4" />
<img width="1920" height="1020" alt="Screenshot 2026-06-17 113038" src="https://github.com/user-attachments/assets/d05b9cce-9841-43eb-9030-68c1f48b244c" />
<img width="1920" height="1020" alt="Screenshot 2026-06-17 113108" src="https://github.com/user-attachments/assets/9125a4a1-b1e0-4ef5-948e-9e58ab2bccaf" />
<img width="1920" height="1020" alt="Screenshot 2026-06-17 113126" src="https://github.com/user-attachments/assets/2b54992b-993a-4ebc-82e0-de2f12051ac1" />


