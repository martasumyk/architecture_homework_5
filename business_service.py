from fastapi import FastAPI
import time
import requests
from typing import Dict

business_app = FastAPI()

@business_app.get("/health")
def health_check():
    return {"status": "ok"}

@business_app.get("/")
def root():
    return {"description": "Business Logic Service"}

@business_app.post("/process")
def process_data(payload: Dict):
    time.sleep(2)  # Simulate processing
    return {"original": payload, "processed": True}