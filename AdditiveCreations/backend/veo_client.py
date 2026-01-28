"""
Veo is NOT publicly available as an API.

This file simulates Veo behavior while keeping
the interface future-compatible.
"""

import time

def generate_video(image_path: str, veo_prompt: str) -> str:
    # Simulate generation latency
    time.sleep(4)

    # Placeholder demo video
    return (
        "https://storage.googleapis.com/gtv-videos-bucket/sample/ForBiggerJoyrides.mp4"
    )
