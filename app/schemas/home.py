from pydantic import BaseModel

class HomeSchema(BaseModel):
    message: str
    data: dict[str, str] | None