import httpx
from fastapi import HTTPException
import os

from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("LLM_API_KEY")
BASE_URL = os.getenv("LLM_API_BASE_URL")
MODEL_NAME = os.getenv("LLM_MODEL")

async def generate_llm_response(
    messages: list[dict], 
    temperature: float, 
    max_tokens: int
) -> str:
    """
    Calls the Mistral API and returns the AI's text response.
    """
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    
    payload = {
        "model": MODEL_NAME,
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens
    }

    # Using httpx.AsyncClient for non-blocking API calls
    async with httpx.AsyncClient(timeout=30.0) as client:
        try:
            response = await client.post(BASE_URL, headers=headers, json=payload)
            response.raise_for_status() # Raise error for bad status codes
            
            data = response.json()
            # Mistral/OpenAI format: choices[0].message.content
            return data["choices"][0]["message"]["content"]
            
        except httpx.HTTPStatusError as e:
            # If the API returns an error (e.g., rate limit, bad key)
            raise HTTPException(
                status_code=e.response.status_code, 
                detail=f"LLM API Error: {e.response.text}"
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Internal LLM Service Error: {str(e)}")