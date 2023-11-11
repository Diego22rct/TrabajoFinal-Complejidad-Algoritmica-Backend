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
        for node in self.graph:
            print(node, ":", self.graph[node])

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
