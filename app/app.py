import os
from fastapi import FastAPI
import pickle
import numpy as np
from pydantic import BaseModel
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO)

# Obtener la ruta absoluta del directorio actual
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Cargar el modelo desde la carpeta correcta
model_path = os.path.join(BASE_DIR, "model.pkl")

with open(model_path, "rb") as f:
    modelo = pickle.load(f)

# Inicializar FastAPI
app = FastAPI()

# Definir esquema de entrada
class InputData(BaseModel):
    features: list

# Endpoint para predicción
@app.post("/predict/")
def predict(data: InputData):
    X_new = np.array(data.features).reshape(1, -1)
    prediction = modelo.predict(X_new)
    
    # Registrar la solicitud y respuesta
    logging.info(f"Entrada: {data.features}, Predicción: {prediction[0]}")
    
    return {"prediction": int(prediction[0])}