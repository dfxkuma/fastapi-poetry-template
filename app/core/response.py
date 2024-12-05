import functools
from typing import Generic, TypeVar, Any

from fastapi import HTTPException
from pydantic import Field, BaseModel

from app.core.error import ErrorCode
from app.core.pydantic_model import BaseSchema

T = TypeVar("T")


class APIResponse(BaseModel, Generic[T]):
    message: str | None
    data: T | None = None


class SuccessfulEntityResponse(BaseSchema):
    entity_id: str = Field(..., examples=["673c114c-e920-4b6c-bc16-f5666c8d1e60"])


class ErrorResponse(BaseSchema):
    error_code: ErrorCode = Field(..., examples=["USER_NOT_FOUND"])
    message: str = Field(..., examples=["요청한 사용자를 찾을 수 없습니다."])
    error_data: dict = Field(
        default_factory=functools.partial(dict, {}),
        examples=[{"user_id": "673c114c-e920-4b6c-bc16-f5666c8d1e60"}],
    )


class APIError(HTTPException):
    def __init__(
        self,
        status_code: int,
        error_code: ErrorCode,
        message: str,
        error_data: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
    ):
        if error_data is None:
            error_data = {}
        self.error_response = ErrorResponse(
            error_code=error_code.value, message=message, error_data=error_data
        )

        super().__init__(
            status_code=status_code,
            detail=self.error_response.model_dump(exclude_none=True),
            headers=headers,
        )
