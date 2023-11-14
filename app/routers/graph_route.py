from fastapi import APIRouter
import pandas as pd
from app.utils.graph import Grafo

grafo = Grafo()

total_cargado = grafo.importGraphFromFile("app/assets/graph__file/grafo.txt")
print(total_cargado)

router = APIRouter()


@router.get("/graph")
async def get_graph():
    return {"graph": total_cargado}
