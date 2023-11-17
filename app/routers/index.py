from fastapi import APIRouter
import pandas as pd

# from .graph_route import grafo
from . import graph_route as graph_router

# numero_de_animes = 10000

df_anime = pd.read_csv(
    "app/assets/dataset/anime-dataset-2023.csv",
    encoding="utf-8",
)
print("Tamaño del dataset: ", df_anime.shape)
print("Dataset cargado correctamente")


router = APIRouter()

router.include_router(graph_router.router)


def search_anime(anime_name: str):
    """
    Busca un anime en el dataframe df_anime por su nombre.

    Args:
    anime_name (str): El nombre del anime a buscar.

    Returns:
    Si se encuentra el anime, retorna la fila correspondiente del dataframe.
    Si no se encuentra el anime, retorna None.
    """
    for index, row in df_anime.iterrows():
        if row["Name"] == anime_name:
            return row
    return None


def search_anime_by_id(id: int):
    """
    Busca un anime en el dataframe df_anime por su id.

    Args:
        id (int): El id del anime a buscar.

    Returns:
        dict: Un diccionario con la información del anime encontrado o None si no se encontró.
    """
    for index, row in df_anime.iterrows():
        if row["anime_id"] == id:
            return row
    return None


@router.get("/hello")
async def hello():
    """
    Returns a JSON response with a message "Hello, World!".
    """
    return {"message": "Hello, World!"}


@router.get("/anime/{anime_name}")
async def anime_name(anime_name: str):
    """
    Busca un anime por su nombre.

    Args:
    anime_name (str): El nombre del anime a buscar.

    Returns:
    dict: Un diccionario con la información del anime encontrado o un mensaje de error si no se encontró.
    """
    anime = search_anime(anime_name)
    print(anime)
    if anime is None:
        return {"Response": "No se encontro el anime"}
    return {"anime": anime}


@router.get("/anime/{id}")
async def anime_id(id: int):
    """
    Busca un anime por su ID.

    Args:
        id (int): El ID del anime a buscar.

    Returns:
        dict: Un diccionario con la información del anime encontrado o un mensaje de error si no se encontró.
    """
    anime = search_anime_by_id(id)
    if anime is None:
        return {"Response": "No se encontro el anime"}
    return {"anime": anime}


@router.get("/anime/{genre}")
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
