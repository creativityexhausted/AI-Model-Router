from .intent_classifier import classify_intent
from .models.simple_model import simple_answer
from .models.local_model import llama_answer
from .models.gpt_model import gpt_answer

def route_question(question: str):
    category = classify_intent(question)
    print("Predicted category:", category)

    if category == "creative":
        return llama_answer(question)

    elif category == "factual":
        return llama_answer(question)

    elif category == "simple":
        return gpt_answer("Give a short, friendly greeting response to: " + question)

    else:
        return llama_answer(question)  # general → llama for now