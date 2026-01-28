VEO_PROMPT_TEMPLATE = """
{scene}

Camera motion:
{camera}

Lighting:
{lighting}

Style:
{style}

Technical constraints:
- Duration: {duration}s
- FPS: {fps}
- Cinematic realism
- High temporal coherence

Negative:
blurry, jitter, artifacts, distortion, flickering
"""
