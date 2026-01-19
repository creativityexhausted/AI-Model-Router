# 🧠 AI Model Router

A smart, lightweight AI orchestration system that intelligently routes user queries to the most suitable AI model based on intent. Built with **FastAPI**, **Streamlit**, and **Machine Learning**.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.95%2B-009688)
![Streamlit](https://img.shields.io/badge/Streamlit-1.22%2B-FF4B4B)
![Ollama](https://img.shields.io/badge/Ollama-Llama3.2-black)

## 📖 Overview

**AI Model Router** solves the "one model fits all" inefficiency. Instead of sending every query to a massive, expensive model, this system analyzes the user's intent (e.g., Creative, Factual, Simple Greeting) and routes it to a specialized model optimized for that task.

### How It Works
1. **User asks a question** via the Streamlit UI.
2. **Intent Classifier** (Logistic Regression + Sentence Transformers) predicts the category:
   - `Creative` / `Factual` / `General` → **Llama 3.2** (via Ollama)
   - `Simple` / `Greeting` → **Flan-T5 Large** (Hugging Face)
3. **The selected model generates a response.**
4. **The result is displayed** in the modern, dark-themed UI.

---

## ✨ Features

- **🚀 Intelligent Routing:** Uses ML-based embedding classification (not just keywords) to determine user intent.
- **🎨 Modern UI:** A beautiful, dark-themed interface built with Streamlit.
- **⚡ Hybrid AI Architecture:**
  - **Local LLM:** Integrates with **Ollama (Llama 3.2)** for complex tasks.
  - **Hugging Face:** Uses **Google Flan-T5** for quick, creative, or simple conversational tasks.
- **🔌 API-First Design:** Backend is decoupled using FastAPI, allowing for easy expansion.

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit
- **Backend:** FastAPI, Uvicorn
- **ML & NLP:** Sentence-Transformers, Scikit-learn, PyTorch, Hugging Face Transformers
- **LLM Serving:** Ollama (Local Llama 3.2)

---

## 📂 Project Structure

```bash
AI-Model-Router/
├── backend/
│   ├── models/
│   │   ├── gpt_model.py       # Handles Google Flan-T5 logic
│   │   ├── local_model.py     # Handles Ollama (Llama 3.2) logic
│   │   └── simple_model.py    # Fallback/Test model
│   ├── classifier.py          # (Deprecated) Keyword classifier
│   ├── intent_classifier.py   # ML-based Intent Classifier (Logistic Regression)
│   ├── main.py                # FastAPI entry point
│   ├── requirements.txt       # Backend dependencies
│   └── router.py              # Main routing logic
├── frontend/
│   └── app.py                 # Streamlit UI
├── .gitignore
└── README.md
