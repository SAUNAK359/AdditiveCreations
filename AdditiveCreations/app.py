import streamlit as st
from ui.layout import render_ui
from utils.files import persist_uploaded_file
from core.pipeline import generate_video_pipeline

st.set_page_config(layout="wide")

image, prompt, style, duration, fps = render_ui()

if st.button("Generate Video"):
    if not image or not prompt:
        st.error("Image and prompt are required")
    else:
        image_path = persist_uploaded_file(image)

        with st.spinner("Generating cinematic video..."):
            try:
                video_url, veo_prompt = generate_video_pipeline(
                    image_path=image_path,
                    user_prompt=prompt,
                    style=style,
                    duration=duration,
                    fps=fps
                )
                st.video(video_url)

            except NotImplementedError as e:
                st.warning(str(e))

        with st.expander("Optimized Veo Prompt"):
            st.code(veo_prompt)
