from fastapi import FastAPI
from typing import Dict

db_app = FastAPI()

db_store = {}

@db_app.get("/health")
def health_check():
    return {"status": "ok"}

@db_app.get("/")
def root():
    return {"description": "Database Service"}

@db_app.post("/save")
def save_data(payload: Dict):
    key = str(len(db_store) + 1)
    db_store[key] = payload
    return {"message": "Data saved", "key": key}

@db_app.get("/get/{key}")
def get_data(key: str):
    return db_store.get(key, {"error": "Key not found"})