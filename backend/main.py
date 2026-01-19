from fastapi import FastAPI
from .router import route_question

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Model Router Running"}

@app.post("/ask")
def ask_router(question: str):
    # Unpack the tuple here
    answer_text, model_name = route_question(question)
    
    # Return both fields
    return {"answer": answer_text, "model": model_name}