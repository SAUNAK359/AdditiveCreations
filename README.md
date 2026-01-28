# AdditiveCreations
AdditiveCreations
Professional AI Video Generation Platform

OVERVIEW

AdditiveCreations is a professional, future-proof AI video generation platform that converts image and natural language prompts into cinematic video prompts and pipelines. The system is designed to integrate seamlessly with Google Veo once it becomes publicly available.

The platform uses Gemma Flash via the Gemini API for intelligent prompt optimization and is built using an enterprise-grade, modular architecture suitable for production deployment on Streamlit Cloud.

KEY FEATURES

• Prompt Intelligence Layer
Uses Gemma Flash (Gemini API) to convert user intent into Veo-optimized cinematic prompts

• Image-Conditioned Video Generation
Designed for image + prompt → video workflows

• Cinematic Prompt Engineering
Includes camera motion, lighting, realism, and temporal consistency

• Enterprise-Grade Architecture
Clean separation of UI, core logic, providers, and configuration layers

• Single API Key Authentication
Only a Gemini API key is required; no separate Veo key needed

• Cloud Deployable
Works locally and on Streamlit Cloud

ARCHITECTURE OVERVIEW

User
↓
Streamlit UI
↓
Prompt Optimizer (Gemma Flash)
↓
Veo-Optimized Prompt Builder
↓
Video Provider Interface
↓
Veo Provider (API-gated, future-ready)

Note: Google Veo is not publicly available yet. This repository provides a production-ready abstraction layer so Veo can be integrated instantly once released.

REPOSITORY STRUCTURE

AdditiveCreations/

app.py Streamlit entrypoint
requirements.txt
README.txt

config/ Environment and constants
env.py
constants.py

core/ Business logic
prompt_optimizer.py
prompt_builder.py
video_provider.py
pipeline.py

providers/ Model providers
veo.py

ui/ UI components
layout.py
theme.py

utils/ Utilities
files.py
logger.py

assets/
logo.png

API KEY SETUP (IMPORTANT)

Only ONE API key is required.

AdditiveCreations uses the Gemini API key for Gemma Flash prompt optimization.
A separate Veo API key is NOT required.

To obtain a Gemini API key:
https://aistudio.google.com/

STREAMLIT CLOUD SETUP

Add the following secret in your Streamlit app settings:

GOOGLE_API_KEY = YOUR_GEMINI_API_KEY

LOCAL DEVELOPMENT SETUP

Create a .env file in the project root:

GOOGLE_API_KEY=YOUR_GEMINI_API_KEY

RUNNING THE APPLICATION

Install dependencies
pip install -r requirements.txt

Start the application
streamlit run app.py

VEO API STATUS

Google Veo is currently API-restricted.

This repository:
• Implements real Gemma Flash integration
• Implements a correct Veo provider abstraction
• Does NOT include a fake or mocked Veo API

When Veo becomes public, only one file needs to be updated:

providers/veo.py

No architectural changes are required.

DESIGN PRINCIPLES

• No hard-coded secrets
• No mock business logic in the core pipeline
• Provider-based model abstraction
• Logging and validation by default
• Clean upgrade path to Vertex AI

ROADMAP

• Direct Veo API integration
• Multi-shot timeline editor
• User authentication and credit system
• Developer API access
• Vertex AI backend support

USE CASES

• AI video startups
• Creator tools
• Marketing automation
• Research and experimentation
• Portfolio and internship projects
• Pre-API product development

AUTHOR

AdditiveCreations
Built with a production-first mindset for real-world AI systems.

LICENSE

This project is released under the MIT License
