import os
from dotenv import load_dotenv

load_dotenv()

# Gemini / Gemma API key (ONLY key needed)
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if GOOGLE_API_KEY is None:
    raise RuntimeError("GOOGLE_API_KEY not found in environment variables")

APP_NAME = "AdditiveCreations"
APP_TAGLINE = "Professional AI Video Generation"

DEFAULT_DURATION = 8
DEFAULT_FPS = 24
