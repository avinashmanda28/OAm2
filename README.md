# OAm² — AI Video Factory

OAm² is an advanced AI system designed to convert a single prompt into a fully produced long-form video.

The platform automatically performs:

- Research
- Script writing
- Scene planning
- Visual generation
- Voice narration
- Caption generation
- Video editing
- Rendering

The goal is to produce **4–20+ minute videos automatically** from a simple idea.

---

## Core Idea

Idea → Fully Produced Video

Example prompt:

Create a 10 minute YouTube video explaining artificial intelligence.

OAm² automatically generates:

- video script
- scenes
- visuals
- voice narration
- music
- captions
- final video

---

## System Architecture

The system is built using modular AI components:

- Prompt Intelligence
- Research Engine
- Story Engine
- Script Generator
- Scene Planner
- Visual Generator
- Voice Generator
- Video Composer
- Rendering Engine

Each module has fallback systems and a self-healing mechanism to maintain pipeline stability.

---

## Technology Stack

- Python
- FastAPI
- FFmpeg
- Stable Diffusion
- Coqui TTS
- LLMs (Llama / Mistral)
- Google Colab
- GitHub

---

## Development Philosophy

OAm² follows a step-by-step modular architecture.

Every module includes:

- primary implementation
- fallback system
- validation layer

This ensures the video generation pipeline never stops even if a module fails.

---

## Status

Currently under development.
