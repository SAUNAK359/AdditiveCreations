from config.prompt_schema import VEO_PROMPT_TEMPLATE

def build_veo_prompt(optimized_scene, style, duration, fps):
    return VEO_PROMPT_TEMPLATE.format(
        scene=optimized_scene,
        camera="Smooth cinematic dolly, pan, or orbit depending on scene",
        lighting="Physically based lighting, soft global illumination",
        style=style,
        duration=duration,
        fps=fps
    )
