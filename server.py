from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ChatRequest(BaseModel):
    prompt: str

@app.get("/")
def home():
    return {"status":"AI running"}

@app.post("/chat")
def chat(req: ChatRequest):

    return {
        "response":"AI reply: " + req.prompt
    }
