from transformers import pipeline

classifier = pipeline("text-classification", model="bhadresh-savani/bert-base-go-emotion")

def classify_question(question: str):
    q = question.lower()

    if "poem" in q or "story" in q or "write" in q:
        return "creative"

    if "who" in q or "what" in q or "when" in q or "where" in q:
        return "factual"

    if len(q.split()) <= 2:
        return "simple"

    return "general"
