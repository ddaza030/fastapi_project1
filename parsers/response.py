from pydantic import BaseModel
from typing import Optional, Union


class BaseResponse(BaseModel):
    data: str
    status: bool
    message: str
