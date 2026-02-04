import networkx as nx
from database.dao import DAO

class Model:
    def __init__(self):
        self.G = nx.DiGraph()
        self.lista_indici = []
        self.dizionario_nodi={}



    def take_all_ruoli(self):

        lista_ruoli=DAO.query_ruoli()

        return lista_ruoli

    def build_graph(self, role: str):


        self.dizionario_nodi=DAO.get_authorship(role)


        for n in self.dizionario_nodi.values():

            self.G.add_node(n)

        for n1 in self.dizionario_nodi.values():
            for n2 in self.dizionario_nodi.values():

                if n1 != n2:
                    if n1.num_objects != 0 and n2.num_objects != 0:
                        peso=abs(n1.num_objects-n2.num_objects)

                        if n1.num_objects == n2.num_objects:
                            continue

                        if n1.num_objects< n2.num_objects:

                            self.G.add_edge(n1, n2,weight=peso)

                        if n1.num_objects >n2.num_objects:
                            self.G.add_edge(n2, n1,weight=peso)


        return self.G.number_of_nodes(),self.G.number_of_edges()










    def classifica(self):
        pass
