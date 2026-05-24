# Machine Predictive Maintenance Classification System

## 📌 Project Overview

Machine Predictive Maintenance Classification is an AI-powered web application designed to predict industrial machine failures before they occur using Machine Learning algorithms. The system analyzes important machine operational parameters such as air temperature, process temperature, rotational speed, torque, tool wear, and machine type to classify whether a machine is likely to fail or operate normally.

The project helps industries reduce unexpected downtime, improve operational efficiency, lower maintenance costs, and increase equipment lifespan through intelligent predictive analytics.

---

## 🌐 Live Demo 

🚀 Try the Live Application Here:

[Machine Predictive Maintenance Live Demo](https://machine-predictive-maintenance-hmyx.onrender.com/?utm_source=chatgpt.com)

---

Add this section near the top of your README file after the Project Overview section.



# 🚨 Problem Statement

Traditional maintenance systems mainly follow:

* Reactive Maintenance → Fix after failure
* Preventive Maintenance → Regular scheduled maintenance

These methods often lead to:

* Unexpected machine breakdowns
* Increased operational cost
* Production delays
* Wastage of resources
* Human monitoring limitations

Industries require a smarter solution that can:

✅ Detect failure risks early
✅ Reduce downtime
✅ Improve productivity
✅ Automate monitoring
✅ Optimize maintenance schedules

This project solves these challenges using Machine Learning-based predictive maintenance.

---

# 🎯 Objectives

* Predict machine failure using ML classification models
* Build a real-time industrial monitoring system
* Provide a user-friendly web interface
* Reduce maintenance cost and downtime
* Demonstrate practical AI implementation in Industry 4.0

---

# 🏭 Real-World Use Cases

## Manufacturing Industries

Predict failures in CNC machines, motors, turbines, and production equipment.

## Automotive Industries

Monitor assembly line machines and industrial robotics.

## Smart Factories

Integrate predictive analytics into IoT-enabled systems.

## Power Plants

Monitor heavy equipment and rotating machinery.

## Industrial Automation

Improve reliability of automated systems.

---

# ⚙ Features

## 🤖 Machine Learning Prediction

* Predicts machine failure in real-time
* Supports multiple machine parameters
* Uses trained ML classification models

## 📊 Smart Input System

* Valid parameter ranges
* Industrial units included
* Guided user input

## 🎨 Modern Frontend

* Glassmorphism UI
* Responsive Design
* Interactive Dashboard
* Animated Effects

## ⚡ Backend API

* Flask REST API
* JSON-based prediction requests
* Fast inference system

---
# deploy
* Render

# 🧠 Machine Learning Models Used

## Random Forest Classifier

Used for ensemble-based classification with high accuracy.

## Bagging Classifier

Used to improve model stability and reduce variance.

---

# 🔄 Sampling Techniques Used

To handle class imbalance:

* RandomOverSampler
* SMOTE
* BorderlineSMOTE
* ClusterCentroids
* Tomek Links
* NearMiss

---

# 📂 Dataset Features

| Feature             | Description                     | Unit       |
| ------------------- | ------------------------------- | ---------- |
| Air Temperature     | Environmental temperature       | Kelvin (K) |
| Process Temperature | Operational process temperature | Kelvin (K) |
| Rotational Speed    | Machine rotational speed        | RPM        |
| Torque              | Rotational force                | Nm         |
| Tool Wear           | Tool usage duration             | Minutes    |
| Machine Type        | Quality category                | L / M / H  |

---

# 🏗 Project Architecture

```bash
Frontend (HTML/CSS/JS)
        ↓
Flask Backend API
        ↓
Machine Learning Model (.pkl)
        ↓
Prediction Result
```

---

# 🛠 Tech Stack

## Frontend

* HTML5
* CSS3
* JavaScript

## Backend

* Flask
* Flask-CORS

## Machine Learning

* Scikit-learn
* Imbalanced-learn
* NumPy
* Pandas

## Model Persistence

* Pickle (.pkl)

---

# 📁 Project Structure

```bash
ml-classification-project/
│
├── backend/
│   ├── app.py
│   ├── routes/
│   │   └── predict.py
│   ├── models/
│   │   ├── rf_model.pkl
│   │   └── bag_model.pkl
│   └── requirements.txt
│
├── frontend/
│   └── index.html
│
├── dataset/
│   └── machine_data.csv
│
├── notebook/
│   └── training.ipynb
│
└── README.md
```

---

# 🚀 Installation Guide

## 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/machine-predictive-maintenance.git
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

---

## 3️⃣ Activate Environment

### Windows

```bash
venv\\Scripts\\activate
```

### Linux/Mac

```bash
source venv/bin/activate
```

---

## 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 5️⃣ Run Backend Server

```bash
cd backend
python app.py
```

---

## 6️⃣ Run Frontend

Open:

```bash
frontend/index.html
```

or use Live Server extension in VS Code.

---

# 🔌 API Endpoint

## POST `/predict`

### Request Body

```json
{
  "features": [300, 310, 1500, 40, 10, 1]
}
```

### Response

```json
{
  "prediction": "No Machine Failure"
}
```

---

# 📈 Example Predictions

## Safe Machine Example

```json
[300, 310, 1500, 40, 10, 1]
```

Result:

```bash
No Machine Failure
```

---

## Failure Risk Example

```json
[325, 340, 3200, 95, 280, 0]
```

Result:

```bash
Machine Failure
```

---

# 🧪 Model Training Workflow

1. Data Cleaning
2. Feature Selection
3. Handling Imbalanced Dataset
4. Model Training
5. Hyperparameter Tuning
6. Model Evaluation
7. Model Saving
8. Deployment

---

# 📊 Evaluation Metrics

* F1 Score
* ROC-AUC Score
* Accuracy
* Cross Validation

---

# ⏱ Development Time

| Task                        | Time    |
| --------------------------- | ------- |
| Data Preprocessing          | 6 Hours |
| Model Training & Evaluation | 8 Hours |
| Backend Development         | 4 Hours |
| Frontend UI Development     | 7 Hours |
| Authentication System       | 2 Hours |
| Testing & Debugging         | 5 Hours |

## ✅ Total Time Taken: 3 Days

---

# 🔥 Future Improvements

* JWT Authentication
* Database Integration
* Cloud Deployment
* Docker Support
* Real-time IoT Integration
* Live Sensor Monitoring
* Deep Learning Models
* Admin Dashboard
* Prediction Analytics

---

# 👨‍💻 Author

### Ankana Sadhukhan

AI/ML Developer | Full Stack Developer | Open Source Contributor

---

# ⭐ Conclusion

This project demonstrates how Artificial Intelligence and Machine Learning can transform industrial maintenance systems by enabling predictive analytics and intelligent failure detection. The system provides a practical implementation of Industry 4.0 concepts using modern web technologies and machine learning techniques.

---

# 🌟 If you like this project, give it a star on GitHub!
