from fastapi import APIRouter, File
from fastapi import Body, UploadFile
import pandas as pd


from parsers.table import Tabla
from parsers.response import BaseResponse
from utils.tablas import map_animal

router = APIRouter(
    prefix='/items'
)


@router.put('/registros/anadir', tags=["users"], response_model=BaseResponse)
async def actualizar(registros: UploadFile = File(...)):
    try:
        response = {
            'data': map_animal(registros).read(),
            'message': 'eso es todo',
            'code': 200
        }
        print('bien')
    except KeyError as e:
        response = {
            'message': 'las columnas de las tablas no corresponden',
            'code': 400,
            'data': None
        }
        print('szs')
    except Exception as e:
        response = {
            'message': repr(e),
            'code': 400,
            'data': None
        }
        print(e)
    finally:
        print(response)
        return response
