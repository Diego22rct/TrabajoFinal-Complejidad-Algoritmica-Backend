from app.utils.graph import Grafo
import pandas as pd

grafo = Grafo()
total_cargado = grafo.import_graph_from_file("app/assets/graph__file/grafo_anime.csv")


df_anime = pd.read_csv(
    "app/assets/dataset/anime-dataset-2023.csv",
    encoding="utf-8",
)
print("Tamaño del dataset: ", df_anime.shape)
print("Dataset cargado correctamente")
