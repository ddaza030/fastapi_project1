from pydantic import BaseModel
from fastapi import UploadFile
from typing import Optional


class BaseResponse(BaseModel):
    data: bytes
    code: int
    message: str
