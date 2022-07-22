from fastapi import APIRouter, File
from fastapi import Body, UploadFile, Request
import pandas as pd


from parsers.table import Tabla
from parsers.response import BaseResponse
from utils.tablas import map_animal

router = APIRouter(
    prefix='/items'
)


@router.put('/registros/anadir', tags=["users"], response_model=BaseResponse)
async def actualizar(request: Request, registros: UploadFile = File(...)):
    # TODO: manera correcta de pasar la respuesta o de mostrar errores
    try:
        response = {
            'data': map_animal(registros, request).read(),
            'message': 'eso es todo',
            'code': 200
        }
    except KeyError as e:
        response = {
            'message': 'las columnas de las tablas no corresponden',
            'code': 400,
            'data': None
        }
    except Exception as e:
        response = {
            'message': repr(e),
            'code': 400,
            'data': None
        }
    finally:
        return response
