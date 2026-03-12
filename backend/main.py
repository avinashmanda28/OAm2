from fastapi import FastAPI

app = FastAPI(
    title="OAm² AI Video Factory",
    version="1.0"
)

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
