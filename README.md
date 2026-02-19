# 🎗️ Cervical Cancer Risk Prediction System

This project is an end-to-end Machine Learning application designed to predict the risk of cervical cancer based on clinical and demographic data. The project includes a complete data science pipeline, from data preprocessing and handling class imbalance to deploying an interactive web dashboard.

## 🚀 Features
- **Machine Learning Model:** Utilizes a **Random Forest Classifier** achieving an accuracy of **96.2%**.
- **Class Imbalance Handling:** Implemented **SMOTE** (Synthetic Minority Over-sampling Technique) to ensure the model learns effectively from minority cases.
- **Interactive Dashboard:** A professional web interface built with **Streamlit** for real-time risk assessment.
- **Medical Recommendations:** Provides specialized action steps based on the predicted risk level.
- **Data Visualization:** Includes interactive gauges and charts using **Plotly**.

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Core Libraries:** Pandas, NumPy, Scikit-learn, Imbalanced-learn.
- **Visualization:** Plotly, Seaborn, Matplotlib.
- **Deployment:** Streamlit.

## 📁 Project Structure
- `cancer.ipynb`: Jupyter Notebook containing EDA, data cleaning, and model training.
- `app.py`: The main Streamlit application script for the web dashboard.
- `model.pkl`: The saved Random Forest model.
- `features.pkl`: List of feature names used during training.
- `medians.pkl`: Saved median values for handling missing data in real-time.

## 📊 Dataset
The model was trained on the **Cervical Cancer (Risk Factors)** dataset. It includes features like age, smoking habits, medical history (STDs), and previous screening results.
