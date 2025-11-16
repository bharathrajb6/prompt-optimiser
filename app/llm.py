import requests
import json

# Ollama settings
LLM_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.2"   # change to "llama3.2:3b" if needed


def optimisePrompt(query):
    prompt = f"""
You are an expert AI assistant. Re-write the current prompt that AI Models should understand easily and efficiently produce te output.
Also, dont add un-necessary data in the prompt. If the prompt is related to the design of the software or anything then add design related things in the optimised prompt.
If they ask any question please don't answer it. Your main job is to optimise the prompt.
### Prompt:
{query}

### Answer:
"""

    # Call Ollama
    response = requests.post(
        LLM_URL,
        json={"model": MODEL, "prompt": prompt}
    )

    raw = response.text

    # ---- FIX: Parse streaming JSON lines ----
    final_answer = ""

    for line in raw.splitlines():
        line = line.strip()
        if not line:
            continue

        try:
            obj = json.loads(line)
            final_answer += obj.get("response", "")
        except json.JSONDecodeError:
            # Ignore malformed lines (rare but safe)
            continue

    return final_answer if final_answer.strip() else "No answer generated."