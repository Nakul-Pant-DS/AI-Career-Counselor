from fastapi import FastAPI

from app.core.config import settings
from app.routers.resume import router as resume_router

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Enterprise AI Career Counselor Platform"
)

app.include_router(
    resume_router,
    prefix=settings.API_PREFIX
)


@app.get("/")
def home():
    return {
        "message": f"Welcome to {settings.APP_NAME}"
    }


@app.get("/health")
def health():
    return {
        "status": "Application is running",
        "environment": settings.ENVIRONMENT,
        "version": settings.APP_VERSION
    }
