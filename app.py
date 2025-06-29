from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from joblib import load
import pandas as pd
import os

app = FastAPI()
model_path = "model.pkl"

# Load model at startup
model = load(model_path)

class JobFeatures(BaseModel):
    engineer_id: int
    job_type: str
    job_priority: str
    engineer_skill_level: int
    engineer_experience_years: int
    distance_km: float

@app.post("/predict")
def predict(features: JobFeatures):
    try:
        df = pd.DataFrame([features.dict()])
        df_encoded = pd.get_dummies(df)  # ensure alignment with training features
        prediction = model.predict(df_encoded)[0]
        return {"predicted_success": int(prediction)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))