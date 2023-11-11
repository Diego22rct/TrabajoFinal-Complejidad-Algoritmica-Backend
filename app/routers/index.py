from fastapi import APIRouter
import pandas as pd

numero_de_animes = 1000

df_anime = pd.read_csv(
    "app/assets/dataset/anime-dataset-2023.csv",
    encoding="utf-8",
    nrows=numero_de_animes,
)
print("Tamaño del dataset: ", df_anime.shape)
print("primera fila del dataset: ", df_anime.iloc[0])

router = APIRouter()


def search_anime(anime_name: str):
    # buscar en el dataset
    # retornar el anime
    for index, row in df_anime.iterrows():
        if row["Name"] == anime_name:
            return row
    return None


def search_anime_by_id(id: int):
    # buscar en el dataset
    # retornar el anime
    for index, row in df_anime.iterrows():
        if row["anime_id"] == id:
            return row
    return None


@router.get("/hello")
async def root():
    return {"message": "Hello, World!"}


@router.get("/anime/{anime_name}")
async def root(anime_name: str):
    # buscar en el dataset
    # retornar el anime

    anime = search_anime(anime_name)
    print(anime)
    if anime is None:
        return {"Response": "No se encontro el anime"}
    return {"anime": anime}


@router.get("/anime/id/{id}")
async def root(id: int):
    # buscar en el dataset
    # retornar el anime
    anime = search_anime_by_id(id)
    if anime is None:
        return {"Response": "No se encontro el anime"}
    return {"anime": anime}
