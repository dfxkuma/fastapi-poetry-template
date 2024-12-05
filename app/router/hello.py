from fastapi import APIRouter
from fastapi_restful.cbv import cbv

from app.core.response import APIResponse

router = APIRouter(
    prefix="/hello",
    tags=["Hello"],
    responses={404: {"description": "Not found"}},
)


@cbv(router)
class Hello:

    @router.get("/world")
    async def get_home(self) -> APIResponse[dict]:
        return APIResponse(
            message="Hello, World!",
            data={"message": "Hello, World!"},
        )
