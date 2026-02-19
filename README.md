# 🎗️ Cervical Cancer Risk Prediction System

This project provides a complete Machine Learning solution to predict cervical cancer risk. It includes a data analysis pipeline and an interactive Streamlit dashboard for real-time predictions.

## 📊 Project Workflow

### Data Preprocessing & Cleaning
* **Handling Missing Values:** Replaced `?` values with `NaN` and imputed them using the **Median** of each column.
* **Feature Selection:** Dropped redundant columns like `STDs: Time since first diagnosis` and `STDs: Time since last diagnosis` due to high missing ratios.
* **Type Conversion:** Converted all object columns to numeric for model compatibility.

### Imbalance Handling
* Since the dataset was highly imbalanced, **SMOTE** (Synthetic Minority Over-sampling Technique) was applied to the training data to improve the detection of positive cancer cases.

### Machine Learning Model
* **Algorithm:** Random Forest Classifier.
- **Evaluation Metrics (Test Set):**
  - **Accuracy:** 96.2%
  - **Precision/Recall:** Optimized for clinical risk assessment.
- **Serialization:** Model and preprocessing parameters are saved as `.pkl` files for deployment.

### Interactive Dashboard (Streamlit)
* **Real-time Input:** Users can input patient data (Age, Smokes, STDs, etc.) via a sidebar.
* **Risk Visualization:** Displays a **Gauge Chart** (Risk Level %) using Plotly.
* **Clinical Recommendations:** Automatically provides medical advice (e.g., Biopsy or follow-up) based on the prediction.

### 📁 Project Structure
- `cancer.ipynb`: Jupyter Notebook containing EDA, data cleaning, and model training.
- `app.py`: The main Streamlit application script for the web dashboard.
- `model.pkl`: The saved Random Forest model.
- `features.pkl`: List of feature names used during training.
- `medians.pkl`: Saved median values for handling missing data in real-time.

### 📊 Dataset
The model was trained on the **Cervical Cancer (Risk Factors)** dataset. It includes features like age, smoking habits, medical history (STDs), and previous screening results.

**Disclaimer:** This tool is for educational purposes and should not replace professional medical diagnosis.
