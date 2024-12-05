from fastapi import APIRouter

from app.core.config import settings
from app.router.hello import router as hello_router

router = APIRouter(
    responses={404: {"description": "Not found"}},
)


@router.get("/")
def root():
    return {"message": f"Hello, {settings.PROJECT_NAME}"}


router.include_router(hello_router)
