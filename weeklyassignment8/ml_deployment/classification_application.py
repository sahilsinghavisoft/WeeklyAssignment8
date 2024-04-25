from fastapi import FastAPI
import mongoengine
from ml_deployment.utils.filesloader import scaler, model
from ml_deployment.utils.v1.preprocessing_utils import helper_scale_input_features
from ml_deployment.model.mobile_classification_model import InputFeatures
from ml_deployment.model.mongo_data1 import PredictionData
from ml_deployment.config.v1.database_config import mongo_config

# Connect to MongoDB
mongoengine.connect(db="mobile_classification", host=mongo_config.mongo_host)

app = FastAPI()

async def predict_mobile_range(features):
    scaled_inputs = helper_scale_input_features(
        [
            features.battery_power,
            features.fc,
            features.int_memory,
            features.mobile_wt,
            features.n_cores,
            features.pc,
            features.ram,
            features.talk_time,
            features.sc_size,
            features.pixels
        ],
        scaler,
    )
    prediction = model.predict(scaled_inputs)
    prediction = int(prediction[0])
    return prediction

# Endpoint to predict mobile range
@app.post("/predict/")
async def predict(features: InputFeatures):
    prediction = await predict_mobile_range(features)
    
    # Mapping prediction to labels
    if prediction == 0:
        predicted_label = "Low_Budget"
    elif prediction == 1:
        predicted_label = "Normal_range"
    elif prediction == 2:
        predicted_label = 'Mid_range'
    else:
        predicted_label = "Flagship"

    # Saving prediction data
    mobile_data = PredictionData(
        battery_power=features.battery_power,
        fc=features.fc,
        int_memory=features.int_memory,
        mobile_wt=features.mobile_wt,
        n_cores=features.n_cores,
        pc=features.pc,
        ram=features.ram,
        talk_time=features.talk_time,
        sc_size=features.sc_size,
        pixels=features.pixels,
        prediction=predicted_label
    ) 
    
    try:
        mobile_data.save()
    except Exception as e:
        print(f"Error saving prediction data to MongoDB: {e}")
    
    return {"prediction": predicted_label}

# Health check endpoint
@app.get("/health")
def health_check():
    return {"status": True}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
