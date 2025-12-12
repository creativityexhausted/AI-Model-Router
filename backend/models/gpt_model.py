from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "google/flan-t5-large"   # stronger & better

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

def gpt_answer(prompt: str):
    try:
        creative_prompt = (
            "Write a detailed, vivid, imaginative, and descriptive response.\n"
            "Expand the idea fully with rich sensory details and creativity.\n\n"
            f"User request: {prompt}\n"
            "Creative answer:"
        )

        inputs = tokenizer(creative_prompt, return_tensors="pt")

        outputs = model.generate(
            **inputs,
            max_new_tokens=300,
            do_sample=True,
            temperature=1.1,
            top_p=0.92,
            top_k=50,
            repetition_penalty=1.8,
            no_repeat_ngram_size=3
        )

        return tokenizer.decode(outputs[0], skip_special_tokens=True)

    except Exception as e:
        return f"Local FLAN-T5 error: {e}"
