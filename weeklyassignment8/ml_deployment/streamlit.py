import ml_deployment.streamlit as st
import requests
from ml_deployment.model.mobile_classification_model import InputFeatures


FASTAPI_URL = "http://127.0.0.1:8000"

def predict_mobile_range(features):
    response = requests.post(f"{FASTAPI_URL}/predict/", json=features.dict())
    if response.status_code == 200:
        return response.json()["prediction"]
    else:
        return "Error: Failed to get prediction from the server."


def main():
    st.title("Mobile Range Prediction")

    st.write("Enter the features of the mobile device:")
   
    battery_power = st.slider("Battery Power", min_value=500, max_value=2000, step=1)
    fc = st.slider("Front Camera (MP)", min_value=0, max_value=20, step=1)
    int_memory = st.slider("Internal Memory (GB)", min_value=1, max_value=256, step=1)
    mobile_wt = st.slider("Mobile Weight (g)", min_value=80, max_value=200, step=1)
    n_cores = st.slider("Number of Cores", min_value=1, max_value=8, step=1)
    pc = st.slider("Primary Camera (MP)", min_value=0, max_value=20, step=1)
    ram = st.slider("RAM (MB)", min_value=256, max_value=8192, step=256)
    talk_time = st.slider("Talk Time (hrs)", min_value=2, max_value=20, step=1)
    sc_size = st.slider("Screen Size (inches)", min_value=3, max_value=7, step=0.1)
    pixels = st.slider("Pixels Resolution (MP)", min_value=0, max_value=30, step=1)

    # Button to trigger prediction
    if st.button("Predict"):
        # Create InputFeatures object
        input_features = InputFeatures(
            battery_power=battery_power,
            fc=fc,
            int_memory=int_memory,
            mobile_wt=mobile_wt,
            n_cores=n_cores,
            pc=pc,
            ram=ram,
            talk_time=talk_time,
            sc_size=sc_size,
            pixels=pixels
        )
        prediction = predict_mobile_range(input_features)

        st.write(f"Predicted Mobile Range: {prediction}")

if __name__ == "__main__":
    main()
