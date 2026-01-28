from core.video_provider import VideoProvider
from utils.logger import logger

class VeoProvider(VideoProvider):
    """
    Veo provider implementation.
    This will directly map to Google's Veo API when publicly released.
    """

    def generate(self, image_path, prompt, duration, fps):
        logger.info("VeoProvider invoked (API gated)")

        # REAL IMPLEMENTATION WILL LIVE HERE
        # Until Veo is public, this provider is intentionally abstract

        raise NotImplementedError(
            "Veo API is not publicly available yet"
        )
