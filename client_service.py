from fastapi import FastAPI, Header, HTTPException
from business_service import process_data, call_llm
from db_service import save_data
import os
from dotenv import load_dotenv
from typing import Dict

load_dotenv()
APP_TOKEN = os.getenv("APP_TOKEN")

client_app = FastAPI()

@client_app.get("/health")
def health_check():
    return {"status": "ok"}

@client_app.get("/")
def root():
    return {"description": "Client Service"}

@client_app.get("/process")
def orchestrate(authorization: str = Header(None)):
    if authorization != f"Bearer {APP_TOKEN}":
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    data = {"message": "Hello, World!"}
    processed_data = process_data(data)
    save_response = save_data(processed_data)
    
    return {"processed_data": processed_data, "save_response": save_response}

@client_app.post("/query-llm")
def query_llm(payload: Dict, authorization: str = Header(None)):
    if authorization != f"Bearer {APP_TOKEN}":
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    llm_response = call_llm(payload)
    return {"llm_response": llm_response}