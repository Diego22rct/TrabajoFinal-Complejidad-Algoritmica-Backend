import pandas as pd


class Grafo:
    def __init__(self):
        self.graph = {}

    def addNode(self, node):
        if node not in self.graph:
            self.graph[node] = {}

    def addEdge(self, origen, fin, peso):
        self.addNode(origen)
        self.addNode(fin)
        self.graph[origen][fin] = peso
        self.graph[fin][origen] = peso

    def printGraph(self):
        # imprimir un inidice comenzando en 1 luego el nodo y sus adyacentes
        print("Grafo:")
        indice_linea = 1
        for node, edges in self.graph.items():
            indice_nodo2 = 1
            print(f"{indice_linea}: {node}:")
            for edge, weight in edges.items():
                print(f"  {indice_nodo2}. {edge} ({weight})")
                indice_nodo2 += 1
            indice_linea += 1

    def exportTo(self, filename):
        """
        Export the graph to a CSV file with utf-8 encoding.

        Args:
            filename (str): The name of the file to export to.
        """

        # Create a DatzaFrame from the graph dictionary
        df = pd.DataFrame.from_dict(self.graph, orient="index").stack().reset_index()
        df.columns = ["Source", "Target", "Weight"]

        # Export the DataFrame to a CSV file
        df.to_csv(filename, encoding="utf-8", index=False)

    def exportGraphToDict(self):
        """
        Export the graph to a dictionary.

        Returns:
            dict: The graph dictionary.
        """
        graf_to_dict = pd.dict(self.graph)
        graf_to_dict.to_csv("graph_matrix", encoding="utf-8", index=False)

    def importGraphFromFile(self, file_path):
        """
        TODO: arreglar la importacion desde el archivo
        """
        self.graph = {}  # Limpiar el grafo actual
        node_count = 1
        try:
            with open(file_path, encoding="utf-8") as file:
                for line in file:
                    parts = line.strip().split(": {", 1)
                    node_count += 1
                    node, value_str = parts

                    self.addNode(node)
                    for edge in value_str.split(", "):
                        edge_parts = edge.strip().split(" ", 1)
                        if len(edge_parts) == 2:
                            fin, peso = edge_parts
                            peso = peso[:-1]
                            self.addEdge(node, fin, peso)
        except FileNotFoundError:
            print("File not found")
        except Exception as e:
            print("Error occurred:", str(e))

        return node_count
