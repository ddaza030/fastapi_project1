import pandas as pd


def map_animal(df: pd.DataFrame):
    diccionario = {'1': 'perro', '2': 'gato', '3': 'pajaro'}
    df['animal'] = df['animal_id'].map(diccionario)
    return df
