import google.generativeai as genai
from config.settings import GOOGLE_API_KEY
genai.configure(api_key=GOOGLE_API_KEY)

# Use Gemma Flash (fast, cheap, prompt-engineering friendly)
MODEL_NAME = "models/gemma-2-2b-it"

model = genai.GenerativeModel(MODEL_NAME)

def optimize_prompt(user_prompt: str, style: str, duration: int, fps: int) -> str:
    system_prompt = f"""
You are a professional cinematic prompt engineer for Google Veo.

TASK:
Rewrite the user's idea into a Veo-optimized video generation prompt.

INCLUDE:
- Clear scene description
- Camera motion
- Lighting and realism
- Temporal consistency
- Style: {style}
- Duration: {duration} seconds
- FPS: {fps}

OUTPUT:
A single detailed paragraph. No explanations.
"""

    response = model.generate_content(
        f"{system_prompt}\nUSER PROMPT:\n{user_prompt}"
    )

    return response.text.strip()
