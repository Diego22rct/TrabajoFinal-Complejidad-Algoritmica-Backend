from fastapi import APIRouter
import pandas as pd
from app.utils.graph import Grafo

grafo = Grafo()

total_cargado = grafo.import_graph_from_file("app/assets/graph__file/grafo_anime.csv")
# print(total_cargado)
# grafo.print_graph()

router = APIRouter()


@router.get("/graph")
async def get_graph():
    """
    Returns a dictionary containing the graph data.

    Returns:
    dict: A dictionary containing the graph data.
    """
    return {"graph": total_cargado}


@router.get("/anime/two_recomend/{start}/{end}")
async def dijkstra_shortest_path(start, end):
    """
    Encuentra el camino más corto entre dos animes utilizando el algoritmo de Dijkstra.

    Args:
        start (str): El anime de inicio.
        end (str): El anime de destino.

    Returns:
        dict: Un diccionario que contiene los animes recomendados y los animes consultados.
    """
    if start not in grafo.graph:
        return {"error": f"Anime '{start}' not found"}
    if end not in grafo.graph:
        return {"error": f"Anime '{end}' not found"}

    short_path, _ = grafo.dijkstra_shortest_path(start, end)
    if short_path and _ is None:
        return {"error": "No se encontro el camino"}
    return {"animes_recomendados": short_path, "animes_consultados": _}
