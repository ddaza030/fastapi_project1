from pydantic import BaseModel
from fastapi import UploadFile
from typing import Optional


class BaseResponse(BaseModel):
    data: Optional[UploadFile] = None
    code: int
    message: str
