from pydantic import BaseModel
from fastapi import UploadFile, File


class Tabla(BaseModel):
    registros: UploadFile = File(...)
