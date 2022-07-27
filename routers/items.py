from fastapi import APIRouter, File, HTTPException
from fastapi import Body, UploadFile, Request
from fastapi.responses import JSONResponse
import pandas as pd

from parsers.table import Tabla
from parsers.response import BaseResponse
from utils.tablas import map_animal

router = APIRouter(prefix='/items')


class Error(Exception):
    def __init__(self, name: str):
        self.name = name


@router.put('/registros/anadir',
            tags=["users"],
            response_model=BaseResponse,
            status_code=200)
async def actualizar(request: Request, registros: UploadFile = File(...)):
    try:
        data = map_animal(registros, request).read()
    except Exception as e:
        raise HTTPException(status_code=500, detail="error interno")
    else:
        respuesta = {'data': data,
                     'message': 'se devuelve tal',
                     'status': True}
        return respuesta

