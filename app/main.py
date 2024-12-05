from contextlib import asynccontextmanager
from typing import AsyncGenerator

import sentry_sdk
from fastapi import FastAPI

from app.logger import use_logger
from app.core.config import settings
from app.router import router as api_router

logger = use_logger(__name__)


if settings.SENTRY_DSN and settings.ENVIRONMENT != "local":
    sentry_sdk.init(dsn=str(settings.SENTRY_DSN), enable_tracing=True)


def bootstrap() -> FastAPI:
    @asynccontextmanager
    async def lifespan(application: FastAPI) -> AsyncGenerator[None, None]:
        logger.info("Starting application")
        logger.info("Container Wiring complete")
        yield
        logger.info("Shutting down application")
        logger.info("Application shutdown complete")

    app = FastAPI(
        title=settings.PROJECT_NAME,
        lifespan=lifespan,
        docs_url="/api/docs",
        redoc_url=None,
        openapi_url=f"{settings.API_V1_STR}/openapi.json",
        debug=settings.ENVIRONMENT == "local",
    )
    return app


server = bootstrap()
server.include_router(api_router, prefix=settings.API_V1_STR)
