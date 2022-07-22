from pydantic import BaseModel
from typing import Optional, Union


class BaseResponse(BaseModel):
    data: Union[bytes, None]
    code: int
    message: str
