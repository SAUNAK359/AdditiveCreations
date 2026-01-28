import streamlit as st
from ui.styles import load_css

def render_header():
    st.markdown(load_css(), unsafe_allow_html=True)
    st.title("🎬 AdditiveCreations")
    st.caption("Professional AI Video Generation")

def render_controls():
    image = st.file_uploader("Upload Reference Image", ["png", "jpg"])
    prompt = st.text_area("Describe your scene")

    with st.expander("Advanced Controls"):
        style = st.selectbox("Style", ["Cinematic", "Anime", "Photorealistic"])
        duration = st.slider("Duration (seconds)", 4, 12, 8)
        fps = st.selectbox("FPS", [24, 30])

    return image, prompt, style, duration, fps
