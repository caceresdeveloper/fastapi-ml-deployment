# fastapi-ml-deployment
API REST de ML 

Este repositorio contiene la implementación de una API REST en FastAPI para desplegar un modelo de clasificación.

## 📂 Estructura del Proyecto

📂 fastapi-ml-deployment
│── 📂 app
│   ├── model.pkl                 # Modelo entrenado guardado
│   ├── app.py                     # Código de la API con FastAPI
│── notebook.ipynb                 # Notebook de Google Colab documentando el proceso
│── requirements.txt                # Librerías necesarias
│── README.md                       # Instrucciones del proyecto

## 🚀 Cómo ejecutar

1. Instala las dependencias:
```sh
pip install -r requirements.txt

Ejecuta la API con: 
uvicorn app.app:app --reload

Abre en:

Abre http://127.0.0.1:8000/docs en tu navegador.