from fastapi import  FastAPI
import mongoengine
from ml_deployment.utils.filesloader import scaler, model
from ml_deployment.utils.v1.preprocessing_utils import helper_scale_input_features
from ml_deployment.model.mobile_classification_model import InputFeatures
from ml_deployment.model.mongo_data1 import PredictionData

from ml_deployment.config.v1.database_config import mongo_config
mongoengine.connect(db="mobile_classification", host=mongo_config.mongo_host)

app = FastAPI()
async def predict_mobile_range(features):
  
    scaled_inputs = helper_scale_input_features(
        [
            features.battery_power,
            features.ram,
            features.px_height,
            features.px_width,
            features.sc_h,
            features.sc_w,
            features.talk_time,
            features.three_g,
            features.touch_screen,
            features.wifi,
        ],
        scaler,
    )
    prediction = model.predict(scaled_inputs)
    prediction = int(prediction[0])
@app.post("/predict/")
async def predict(features: InputFeatures):
    prediction = predict_mobile_range(features)
    if prediction == 0:
        predicted_label = "l"
    elif prediction==1:
        predicted_label = "M"
    elif prediction==2:
        predicted_label='H'
    else:
        predicted_label="UH"


    mobile_data = PredictionData(
        battery_power=features.battery_power,
        ram=features.ram,
        px_height=features.px_height,
        px_width=features.px_width,
        sc_h=features.sc_h,
        sc_w=features.sc_w,
        talk_time=features.talk_time,
        three_g=features.three_g,
        touch_screen=features.touch_screen,
        wifi=features.wifi,
        prediction=predicted_label,
    )
    mobile_data.save()
    return {"prediction": predicted_label}


@app.get("/health")
def health_check():
    return {"status": True}
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)