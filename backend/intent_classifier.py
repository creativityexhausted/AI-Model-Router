from sentence_transformers import SentenceTransformer
from sklearn.linear_model import LogisticRegression
import numpy as np

# ---------------------------------------------
# ADDED: Strong greeting detection list
# ---------------------------------------------
GREETING_KEYWORDS = [
    "hi", "hello", "hey", "good morning", "good afternoon", "good evening",
    "what's up", "whats up", "sup", "yo", "greetings", "bye", "goodbye",
    "see you", "how are you"
]
# ---------------------------------------------

# Load embedding model
embedder = SentenceTransformer('all-MiniLM-L6-v2')

# Training data for classifier
training_sentences = [
    # Creative prompts
    "write a poem about love",
    "tell me a magical story",
    "describe a fantasy world",
    "write a short story about a dragon",
    "compose a rhyme about school",

    # Factual prompts
    "who is the president of india",
    "what is the capital of france",
    "when did world war 2 end",
    "define artificial intelligence",
    "what is machine learning",

    # Simple prompts (greetings)
    "hi",
    "hello",
    "hey",
    "good morning",
    "bye",

    # General prompts
    "explain cloud computing",
    "how does blockchain work",
    "tell me about quantum computing",
    "explain photosynthesis",
    "what is climate change"
]

training_labels = [
    "creative", "creative", "creative", "creative", "creative",
    "factual", "factual", "factual", "factual", "factual",
    "simple", "simple", "simple", "simple", "simple",
    "general", "general", "general", "general", "general"
]

# Convert sentences → embeddings
X = embedder.encode(training_sentences)

# Train classifier
clf = LogisticRegression(max_iter=200)
clf.fit(X, training_labels)


def classify_intent(question: str):

    # -----------------------------------------------------------
    # ADDED: Rule-based greeting detection (very accurate)
    # -----------------------------------------------------------
    q = question.lower().strip()

    for word in GREETING_KEYWORDS:
        if q == word or q.startswith(word) or word in q:
            return "simple"
    # -----------------------------------------------------------

    # ML classifier fallback
    emb = embedder.encode([question])
    prediction = clf.predict(emb)[0]
    return prediction