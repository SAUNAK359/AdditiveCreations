import google.generativeai as genai
from config.env import GOOGLE_API_KEY
from utils.logger import logger

genai.configure(api_key=GOOGLE_API_KEY)

# ✅ Correct, supported model
MODEL_NAME = "gemini-2.5-flash"

model = genai.GenerativeModel(MODEL_NAME)

def optimize_prompt(
    user_prompt: str,
    style: str,
    duration: int,
    fps: int
) -> str:
    """
    Converts a user prompt into a Veo-optimized cinematic video prompt.
    """

    logger.info("Optimizing prompt using Gemini 1.5 Flash")

    system_instruction = f"""
You are a senior cinematic prompt engineer for Google Veo.

Rewrite the user's prompt into a professional, Veo-optimized video prompt.

Strict requirements:
- Describe scene details clearly
- Include camera motion (pan, dolly, tracking, etc.)
- Include realistic lighting
- Enforce temporal consistency
- Style: {style}
- Duration: {duration} seconds
- Frame rate: {fps} fps

Output ONLY the optimized prompt text.
"""

    response = model.generate_content(
        contents=[
            {
                "role": "user",
                "parts": [
                    {
                        "text": f"{system_instruction}\nUser prompt: {user_prompt}"
                    }
                ]
            }
        ]
    )

    return response.text.strip()
