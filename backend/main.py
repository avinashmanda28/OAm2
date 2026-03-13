from fastapi import FastAPI
from pydantic import BaseModel

from backend.core.controller import Controller


app = FastAPI(
    title="OAm² AI Video Factory",
    version="1.0"
)


# Initialize controller
controller = Controller()


# Request schema
class VideoRequest(BaseModel):
    prompt: str


@app.get("/")
def root():
    return {
        "system": "OAm²",
        "status": "running",
        "message": "AI Video Factory Ready"
    }


@app.post("/create-video")
def create_video(request: VideoRequest):

    result = controller.create_video(request.prompt)

    return result
