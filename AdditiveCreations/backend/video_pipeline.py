from backend.gemma_flash import optimize_prompt
from backend.prompt_engine import build_veo_prompt
from backend.veo_client import generate_video

def run_pipeline(image_path, user_prompt, style, duration, fps):
    optimized_prompt = optimize_prompt(
        user_prompt=user_prompt,
        style=style,
        duration=duration,
        fps=fps
    )

    veo_prompt = build_veo_prompt(
        raw_prompt=optimized_prompt,
        style=style,
        duration=duration,
        fps=fps
    )

    video_url = generate_video(image_path, veo_prompt)

    return video_url, veo_prompt
