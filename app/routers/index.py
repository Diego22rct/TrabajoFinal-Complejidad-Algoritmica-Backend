from fastapi import APIRouter
import pandas as pd

numero_de_animes = 100

df_anime = pd.read_csv(
    "app/assets/dataset/anime-dataset-2023.csv",
    encoding="utf-8",
    nrows=numero_de_animes,
)
print("Tamaño del dataset: ", df_anime.shape)
print("Dataset cargado correctamente")

router = APIRouter()


def search_anime(anime_name: str):
    for index, row in df_anime.iterrows():
        if row["Name"] == anime_name:
            return row
    return None


def search_anime_by_id(id: int):
    for index, row in df_anime.iterrows():
        if row["anime_id"] == id:
            return row
    return None


@router.get("/hello")
async def hello():
    return {"message": "Hello, World!"}


@router.get("/anime/{anime_name}")
async def anime_name(anime_name: str):
    anime = search_anime(anime_name)
    print(anime)
    if anime is None:
        return {"Response": "No se encontro el anime"}
    return {"anime": anime}


@router.get("/anime/id/{id}")
async def anime_id(id: int):
    anime = search_anime_by_id(id)
    if anime is None:
        return {"Response": "No se encontro el anime"}
    return {"anime": anime}


@router.get("/anime/genre/{genre}")
async def anime_genre(genre: str):
    """
    Retorna una lista de animes que pertenecen al genero especificado.

    Args:
    - genre (str): El genero del anime que se desea buscar.

    Returns:
    - dict: Un diccionario con la lista de animes que pertenecen al genero especificado.
    """
    list_animes = []
    for index, row in df_anime.iterrows():
        if genre in row["Genres"]:
            list_animes.append(row)
    if len(list_animes) == 0:
        return {"Response": "Genero no encontrado"}
    return {"anime": list_animes}
