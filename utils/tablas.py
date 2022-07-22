import io

import pandas as pd
from fastapi import UploadFile


def map_animal(file: UploadFile):
    df = pd.read_csv(file.file, dtype=str)

    diccionario = {'1': 'perro', '2': 'gato', '3': 'pajaro'}
    df['animal'] = df['animal_id'].map(diccionario)

    response_file = io.BytesIO()
    df.to_csv(response_file, index=False)
    response_file.seek(0)
    return response_file
