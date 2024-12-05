from typing import Any
from uuid import UUID

from pydantic import ConfigDict, BaseModel
from pydantic.alias_generators import to_camel

common_config = ConfigDict(
    alias_generator=to_camel, populate_by_name=True, json_encoders={UUID: str}
)


def convert_to_string(data: Any) -> Any:
    from enum import Enum

    if isinstance(data, dict):
        return {
            convert_to_string(key): convert_to_string(value)
            for key, value in data.items()
        }
    elif isinstance(data, list):
        return [convert_to_string(item) for item in data]
    elif isinstance(data, UUID):
        return str(data)
    elif isinstance(data, Enum):
        return data.value
    elif isinstance(data, (str, int, float, bool, type(None))):
        return data
    else:
        return str(data)


class BaseSchema(BaseModel):
    model_config = common_config

    def model_dump(self, *args, **kwargs):
        data = super().model_dump(*args, **kwargs)
        return convert_to_string(data)
