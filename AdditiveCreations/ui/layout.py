import streamlit as st
from ui.theme import inject_theme
from config.constants import APP_NAME, TAGLINE, SUPPORTED_STYLES

def render_ui():
    st.markdown(inject_theme(), unsafe_allow_html=True)

    st.title(f"🎬 {APP_NAME}")
    st.caption(TAGLINE)

    col1, col2 = st.columns(2)

    with col1:
        image = st.file_uploader("Reference Image", ["png", "jpg", "jpeg"])
        prompt = st.text_area("Describe your scene")

    with col2:
        style = st.selectbox("Style", SUPPORTED_STYLES)
        duration = st.slider("Duration (seconds)", 4, 12, 8)
        fps = st.selectbox("FPS", [24, 30])

    return image, prompt, style, duration, fps
