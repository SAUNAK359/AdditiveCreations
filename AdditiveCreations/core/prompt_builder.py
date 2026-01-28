def build_veo_prompt(optimized_prompt: str, duration: int, fps: int) -> str:
    return f"""
{optimized_prompt}

Technical Parameters:
- Duration: {duration} seconds
- Frame Rate: {fps} fps
- Quality: cinematic, ultra-realistic
- Temporal coherence: high
- Motion stability: enforced

Negative Prompt:
blurry, jitter, artifacts, distortion, low quality
"""
