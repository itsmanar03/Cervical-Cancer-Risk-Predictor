import streamlit as st
import joblib
import pandas as pd
import numpy as np
import plotly.graph_objects as go

st.set_config = st.set_page_config(
    page_title="Cervical Cancer Analysis",
    page_icon="🩺",
    layout="wide"
)

@st.cache_resource
def load_model_data():
    model = joblib.load("model.pkl")
    features = joblib.load("features.pkl")
    medians = joblib.load("medians.pkl")
    return model, features, medians

try:
    model, features, medians = load_model_data()
except Exception as e:
    st.error(f"Error loading files: {e}")
    st.stop()

with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/387/387561.png", width=100)
    st.title("Model Dashboard")
    st.markdown("---")
    
    st.metric(label="Model Accuracy", value="96.2%", delta="High Precision")
    st.write("The model was trained using Random Forest Classifier.")
    st.info("Accuracy represents the overall performance on the test dataset.")

st.markdown("<h1 style='text-align: center; color: #2E86C1;'>🩺 Cervical Cancer Risk System</h1>", unsafe_allow_html=True)
st.write("---")

st.subheader("📝 Enter Patient Data")
input_data = {}
cols = st.columns(3)

for i, feature in enumerate(features):
    col_idx = i % 3
    with cols[col_idx]:
        default_val = float(medians.get(feature, 0.0))
        input_data[feature] = st.number_input(f"{feature}", value=default_val)

st.write("---")

if st.button("🔍 Run Full Diagnostic Analysis", use_container_width=True):
    df_input = pd.DataFrame([input_data])[features]
    
    prediction = model.predict(df_input)[0]
    probability = model.predict_proba(df_input)[0][1]

    col_res1, col_res2 = st.columns([1, 1])

    with col_res1:
        st.subheader("📊 Risk Assessment")
        if prediction == 1:
            st.error("### Result: High Risk Detected")
            st.markdown(f"**Confidence Score:** {probability*100:.1f}%")
        else:
            st.success("### Result: Low Risk Detected")
            st.markdown(f"**Confidence Score:** {(1-probability)*100:.1f}%")

        fig = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = probability * 100,
            title = {'text': "Risk Level %"},
            gauge = {
                'axis': {'range': [0, 100]},
                'bar': {'color': "#1f77b4"},
                'steps': [
                    {'range': [0, 30], 'color': "#d4edda"},
                    {'range': [30, 70], 'color': "#fff3cd"},
                    {'range': [70, 100], 'color': "#f8d7da"}
                ],
                'threshold': {
                    'line': {'color': "red", 'width': 4},
                    'thickness': 0.75,
                    'value': 90
                }
            }
        ))
        fig.update_layout(height=300, margin=dict(l=20, r=20, t=50, b=20))
        st.plotly_chart(fig, use_container_width=True)

    with col_res2:
        st.subheader("💡 Professional Recommendations")
        if prediction == 1:
            st.warning("**Immediate Action Steps:**")
            st.write("- Referral for Biopsy and Schiller test.")
            st.write("- Detailed colposcopy examination.")
            st.write("- Investigate history of STDs/Smoking.")
        else:
            st.info("**Preventive Care:**")
            st.write("- Routine Pap smear every 3 years.")
            st.write("- Follow up on HPV vaccination status.")
            st.write("- Maintain healthy lifestyle habits.")