from fastapi import APIRouter
from fastapi import Body
import pandas as pd

from parsers.table import Tabla
from parsers.response import BaseResponse
from utils.tablas import map_animal

router = APIRouter(
    prefix='/items'
)


@router.put('/registros/anadir', tags=["users"], response_model=BaseResponse)
async def actualizar(tabla: Tabla = Body(...)):
    try:
        response = {
            'data': map_animal(tabla['registros']),
            'message': 'eso es todo',
            'code': 200
        }
    except KeyError as e:
        response = {
            'message': 'las columnas de las tablas no corresponden',
            'code': 400
        }
    except Exception as e:
        response = {
            'message': e,
            'code': 400
        }
    finally:
        return response
