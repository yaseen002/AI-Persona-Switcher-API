from fastapi import FastAPI
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("LLM_API_KEY")
BASE_URL = os.getenv("LLM_API_BASE_URL")
MODEl_NAME = os.getenv("LLM_MODEL")
TEMPERATURE = os.getenv("TEMPERATURE")
MAX_TOKENTS = os.getenv("MAX_TOKENS")

app = FastAPI()

@app.get('/')
def read_root():
    return {"Hello": "World"}

@app.get('/health-check')
def health_check():
    return {"Status": "healthy"}