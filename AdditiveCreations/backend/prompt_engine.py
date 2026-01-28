from config.prompt_schema import VEO_PROMPT_TEMPLATE

def build_veo_prompt(raw_prompt, style, duration, fps):
    return VEO_PROMPT_TEMPLATE.format(
        scene=raw_prompt,
        camera="Slow cinematic dolly or pan",
        lighting="Physically accurate, global illumination",
        style=style,
        duration=duration,
        fps=fps
    )
