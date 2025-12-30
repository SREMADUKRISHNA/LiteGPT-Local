import logging
import re
import requests
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="LiteGPT-Local Backend")

# CORS configuration to allow frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    reply: str

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "tinyllama"

# System prompt to enforce behavior
SYSTEM_PROMPT = """You are LiteGPT, a simple local chatbot.
If the user provides their name, acknowledge it once and stop.
Do not repeat names.
Do not create conversations.
Do not invent dialogue.
Do not act like customer support.
Answer only the current user input."""

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    user_message = request.message.strip()
    
    if not user_message:
        raise HTTPException(status_code=400, detail="Message cannot be empty")

    # Name handling logic (Pre-processing)
    # Detect phrases like "my name is", "i am", "i'm"
    patterns = [
        r"my name is\s+(.+)",
        r"i am\s+(.+)",
        r"i'm\s+(.+)"
    ]
    
    detected_name = None
    for pattern in patterns:
        match = re.search(pattern, user_message, re.IGNORECASE)
        if match:
            detected_name = match.group(1).strip()
            # Clean up trailing punctuation
            detected_name = detected_name.rstrip(".!?")
            # Capitalize nicely
            detected_name = detected_name.title()
            break
            
    if detected_name:
        return ChatResponse(reply=f"Nice to meet you, {detected_name}! How can I help you?")

    # Construct prompt ensuring strict separation
    full_prompt = f"{SYSTEM_PROMPT}\n\nUser: {user_message}\n\nAssistant:"

    payload = {
        "model": MODEL,
        "prompt": full_prompt,
        "stream": False,
        "options": {
            "temperature": 0.2,
            "top_p": 0.9,
            "num_predict": 100
        }
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload, timeout=30)
        
        if response.status_code == 200:
            data = response.json()
            ai_reply = data.get("response", "").strip()
            
            # Post-processing to remove hallucinations (Safety net)
            for token in ["User:", "System:", "Assistant:"]:
                if token in ai_reply:
                    ai_reply = ai_reply.split(token)[0].strip()
            
            return ChatResponse(reply=ai_reply)
        else:
            logger.error(f"Ollama API Error: {response.text}")
            raise HTTPException(status_code=500, detail=f"Ollama Error: {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        logger.error(f"Connection error: {e}")
        raise HTTPException(status_code=503, detail="Could not connect to Ollama.")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)