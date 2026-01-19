from .intent_classifier import classify_intent
from .models.simple_model import simple_answer
from .models.local_model import llama_answer
from .models.gpt_model import gpt_answer

def route_question(question: str):
    category = classify_intent(question)
    print("Predicted category:", category)

    if category == "creative":
        # Returns (Answer, Model Name)
        return llama_answer(question), "Llama 3.2 (Local)"

    elif category == "factual":
        return llama_answer(question), "Llama 3.2 (Local)"

    elif category == "simple":
        return gpt_answer("Give a short, friendly greeting response to: " + question), "Google Flan-T5"

    else:
        return llama_answer(question), "Llama 3.2 (Local)"  # general → llama for now