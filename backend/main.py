from fastapi import FastAPI
from .router import route_question

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Model Router Running"}

@app.post("/ask")
def ask_router(question: str):
    answer = route_question(question)
    return {"answer": answer}
