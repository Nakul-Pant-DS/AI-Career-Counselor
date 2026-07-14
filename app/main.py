from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

from app.core.config import settings
from app.core.logging import logger

from app.routers.resume import router as resume_router
from app.routers.career import router as career_router


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Enterprise AI Career Counselor Platform"
)


app.include_router(
    resume_router,
    prefix=settings.API_PREFIX
)

app.include_router(
    career_router,
    prefix=settings.API_PREFIX
)


# ==========================================================
# Home
# ==========================================================

@app.get("/")
def home():

    logger.info("=" * 70)
    logger.info("HOME ENDPOINT HIT")
    logger.info("=" * 70)

    print("=" * 70)
    print("HOME ENDPOINT HIT")
    print("=" * 70)

    return PlainTextResponse("HOME WORKING")


# ==========================================================
# Health
# ==========================================================

@app.get("/health")
def health():

    logger.info("=" * 70)
    logger.info("HEALTH ENDPOINT HIT")
    logger.info("=" * 70)

    print("=" * 70)
    print("HEALTH ENDPOINT HIT")
    print("=" * 70)

    return {
        "status": "Application is running",
        "environment": settings.ENVIRONMENT,
        "version": settings.APP_VERSION
    }