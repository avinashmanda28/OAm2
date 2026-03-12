from fastapi import FastAPI
from backend.core.controller import Controller

app = FastAPI(
    title="OAm² AI Video Factory",
    version="1.0"
)

controller = Controller()


@app.get("/")
def root():
    return {
        "system": "OAm²",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }


@app.post("/generate-video")
def generate_video(prompt: str):

    workflow = controller.process_prompt(prompt)

    return {
        "message": "Workflow created",
        "workflow": workflow
    }
