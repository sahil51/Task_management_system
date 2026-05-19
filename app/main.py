from fastapi import FastAPI
from app.routers import task

app = FastAPI(title="Task Management API", version="1.0.0")

app.get("/health", status_code=200)
def health_check():
    return {"status": "ok"}
app.include_router(task.router)