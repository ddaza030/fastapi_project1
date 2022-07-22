import io

import pandas as pd
from fastapi import UploadFile


def map_animal(file: UploadFile, request):
    df = pd.read_csv(file.file, dtype=str)
    app = request.app
    diccionario = {'1': 'perro', '2': 'gato', '3': 'pajaro'}
    df['animal'] = df['animal_id'].map(diccionario)

    response_file = io.BytesIO()
    df.to_csv(response_file, index=False)
    size = len(df)

    response_file.seek(0)
    text = f'se añadieron {size} filas'

    app.telegram.send_message(text)
    return response_file
