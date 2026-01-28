from core.prompt_optimizer import optimize_prompt
from core.prompt_builder import build_veo_prompt
from providers.veo import VeoProvider
from utils.logger import logger

def generate_video_pipeline(
    image_path: str,
    user_prompt: str,
    style: str,
    duration: int,
    fps: int
):
    logger.info("Starting video generation pipeline")

    optimized = optimize_prompt(
        user_prompt=user_prompt,
        style=style,
        duration=duration,
        fps=fps
    )

    veo_prompt = build_veo_prompt(
        optimized_prompt=optimized,
        duration=duration,
        fps=fps
    )

    provider = VeoProvider()

    video_url = provider.generate(
        image_path=image_path,
        prompt=veo_prompt,
        duration=duration,
        fps=fps
    )

    return video_url, veo_prompt
