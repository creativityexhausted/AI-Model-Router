#def llama_answer(prompt: str):
#    return "Llama model is not available. This is a placeholder factual response."

import requests

def llama_answer(prompt: str):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3.2",
                "prompt": prompt,
                "stream": False        # <---- VERY IMPORTANT FIX
            },
            timeout=180
        )

        if response.status_code != 200:
            return f"Llama Error {response.status_code}: {response.text}"

        data = response.json()

        # Non-streaming mode always returns full text in "response"
        return data.get("response", "No response key found.")

    except Exception as e:
        return f"Llama Exception: {e}"