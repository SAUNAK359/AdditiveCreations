import streamlit as st
from ui.layout import render_header, render_controls
from utils.file_utils import save_uploaded_file
from backend.video_pipeline import run_pipeline

st.set_page_config(layout="wide")

render_header()

image, prompt, style, duration, fps = render_controls()

if st.button("Generate Video"):
    if not image or not prompt:
        st.error("Please upload an image and enter a prompt.")
    else:
        image_path = save_uploaded_file(image)

        with st.spinner("Optimizing prompt & generating video..."):
            video_url, veo_prompt = run_pipeline(
                image_path=image_path,
                user_prompt=prompt,
                style=style,
                duration=duration,
                fps=fps
            )

        st.subheader("Generated Video")
        st.video(video_url)

        with st.expander("Veo Optimized Prompt"):
            st.code(veo_prompt)
