import io

import pandas as pd
from fastapi import UploadFile


def map_animal(file: UploadFile):
    with await file.file.read() as bytes_:
        df = pd.read_csv(bytes_)

    diccionario = {'1': 'perro', '2': 'gato', '3': 'pajaro'}
    df['animal'] = df['animal_id'].map(diccionario)

    response_file = io.BytesIO()
    df.to_csv(response_file)
    return response_file
