from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import numpy as np

app = FastAPI(
    title="Telecom QoS API",
    description="API de prédiction de la dégradation de la QoS pour un réseau 5G",
    version="1.0"
)

# Chargement du modèle (kaykoun f dossier models)
model = joblib.load("models/qos_model.pkl")

class TelecomKPIs(BaseModel):
    SINR: float
    RSSI: float
    Packet_Loss: float
    Bandwidth_Usage: float

@app.post("/predict")
def predict_qos(data: TelecomKPIs):
    input_df = pd.DataFrame([[
        data.SINR, 
        data.RSSI, 
        data.Packet_Loss, 
        data.Bandwidth_Usage
    ]], columns=["SINR", "RSSI", "Packet_Loss", "Bandwidth_Usage"])
    
    prediction = int(model.predict(input_df)[0])
    probability = float(model.predict_proba(input_df)[0][1])
    status = "DÉGRADÉ (Alerte)" if prediction == 1 else "NORMAL (Bon)"
    
    return {
        "prediction": prediction,
        "status": status,
        "probability": round(probability, 4),
        "message": f"Qualité de service : {status} avec une probabilité de {round(probability*100, 2)}%"
    }

@app.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API Telecom QoS. Allez sur /docs pour tester."}