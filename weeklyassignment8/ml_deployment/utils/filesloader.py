import pickle

with open("ml_deployment/Datafiles/model_lr.pkl", "rb") as f:
    model = pickle.load(f)
with open("ml_deployment/Datafiles/scaler.pkl", "rb") as f:
    scaler = pickle.load(f)
