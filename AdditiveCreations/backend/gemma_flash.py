import google.generativeai as genai
from config.settings import GOOGLE_API_KEY

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("gemma-2-flash")

def optimize_prompt(user_prompt, style, duration, fps):
    system_prompt = f"""
You are a professional cinematic prompt engineer for Google Veo.
Rewrite the user prompt into a detailed, structured video generation prompt.

Requirements:
- Cinematic camera motion
- Realistic lighting
- Temporal coherence
- Style: {style}
- Duration: {duration}s
- FPS: {fps}
"""

    response = model.generate_content(
        f"{system_prompt}\nUser Prompt: {user_prompt}"
    )

    return response.text.strip()
