import google.generativeai as genai
from config.env import GOOGLE_API_KEY
from utils.logger import logger

genai.configure(api_key=GOOGLE_API_KEY)

MODEL_NAME = "gemma-2-flash"

model = genai.GenerativeModel(MODEL_NAME)

def optimize_prompt(user_prompt: str, style: str, duration: int, fps: int) -> str:
    logger.info("Optimizing prompt using Gemma Flash")

    system_instruction = f"""
You are a senior cinematic prompt engineer for Google Veo.

Rewrite the user prompt into a professional, Veo-optimized video prompt.
Include:
- Scene details
- Camera motion
- Lighting
- Temporal consistency
- Style: {style}
- Duration: {duration}s
- FPS: {fps}

Output only the optimized prompt.
"""

    response = model.generate_content(
        f"{system_instruction}\nUser Prompt: {user_prompt}"
    )

    return response.text.strip()
