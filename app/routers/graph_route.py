from fastapi import APIRouter
import pandas as pd
from app.utils.graph import Grafo

grafo = Grafo()

grafo.importGraphFromFile()


router = APIRouter()

