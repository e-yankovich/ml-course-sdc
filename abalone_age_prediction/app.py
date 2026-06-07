import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.set_page_config(page_title="Abalone Age Prediction")

@st.cache_resource
def load_model():
    return joblib.load("best_model.joblib")

model = load_model()

st.title("Abalone Age Prediction")
st.write("Predict the number of rings (abalone age proxy).")

with st.form("input_form"):
    sex = st.selectbox("Sex", ["M", "F", "I"])

    length = st.number_input("Length", min_value=0.0, value=0.5, step=0.01)
    diameter = st.number_input("Diameter", min_value=0.0, value=0.4, step=0.01)
    height = st.number_input("Height", min_value=0.0, value=0.15, step=0.005)

    whole_weight = st.number_input("Whole_weight", min_value=0.0, value=0.9, step=0.01)
    shucked_weight = st.number_input("Shucked_weight", min_value=0.0, value=0.35, step=0.01)
    viscera_weight = st.number_input("Viscera_weight", min_value=0.0, value=0.2, step=0.01)
    shell_weight = st.number_input("Shell_weight", min_value=0.0, value=0.25, step=0.01)

    submitted = st.form_submit_button("Predict")

if submitted:
    df = pd.DataFrame([{
        "Sex": sex,
        "Length": length,
        "Diameter": diameter,
        "Height": height,
        "Whole_weight": whole_weight,
        "Shucked_weight": shucked_weight,
        "Viscera_weight": viscera_weight,
        "Shell_weight": shell_weight
    }])

    df["log_Shell_weight"] = np.log1p(df["Shell_weight"])
    df["log_Whole_weight"] = np.log1p(df["Whole_weight"])
    df["Sex_I"] = (df["Sex"] == "I").astype(int)

    final_features = [
        "log_Shell_weight",
        "Shell_weight",
        "Shucked_weight",
        "Viscera_weight",
        "Height",
        "Diameter",
        "Length",
        "log_Whole_weight",
        "Whole_weight",
        "Sex_I"
    ]

    X_input = df[final_features]

    pred = model.predict(X_input)[0]
    st.success(f"Predicted rings: {pred:.2f}")
