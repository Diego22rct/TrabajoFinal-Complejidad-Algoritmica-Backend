from fastapi import APIRouter
import pandas as pd
from app.utils.graph import Grafo

grafo = Grafo()

total_cargado = grafo.import_graph_from_file("app/assets/graph__file/grafo_anime.csv")
print(total_cargado)
grafo.print_graph()

router = APIRouter()


@router.get("/graph")
async def get_graph():
    return {"graph": total_cargado}


@router.get("/anime/two_recomend/{start}/{end}")
async def dijkstra_shortest_path(start, end):
    """
    Encuentra el camino mas corto entre dos recomendaciones de anime.
    Parameters:
        start (String): Nombre del anime
        end (String): NOmbre del anime

    Returns:
        dict: A dictionary containing the recommended animes and the consulted animes.
            - "animes_recomendados" (list): A list of recommended animes.
            - "animes_consultados" (list): A list of consulted animes.

        If no path is found, it returns:
        dict: A dictionary containing the error message.
            - "error" (str): The error message indicating that no path was found.
    """
    short_path, _ = grafo.dijkstra_shortest_path(start, end)
    if short_path is None:
        return {"error": "No se encontro el camino"}
    return {"animes_recomendados": short_path, "animes_consultados": _}
