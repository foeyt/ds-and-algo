from utils.Vertex import Vertex


class ListGraph:
    def __init__(self, edges: list[list[Vertex]]):
        self.__adj_list = dict[Vertex, list[Vertex]]()
        for edge in edges:
            self.add_vertex(edge[0])
            self.add_vertex(edge[1])
            self.add_edge(edge[0], edge[1])


    def size(self):
        return len(self.__adj_list)
    

    def add_edge(self, vet1: Vertex, vet2: Vertex):
        if vet1 not in self.__adj_list or vet2 not in self.__adj_list or vet1 == vet2:
            raise ValueError()
        self.__adj_list[vet1].append(vet2)
        self.__adj_list[vet2].append(vet1)
        

    def add_vertex(self, vet: Vertex):
        if vet in self.__adj_list:
            return
        self.__adj_list[vet] = []


    def remove_edge(self, vet1: Vertex, vet2: Vertex):
        if vet1 not in self.__adj_list or vet2 not in self.__adj_list or vet1 == vet2:
            raise ValueError()
        self.__adj_list[vet1].remove(vet2)
        self.__adj_list[vet2].remove(vet1)


    def remove_vertex(self, vet: Vertex):
        if vet not in self.__adj_list:
            raise ValueError()
        self.__adj_list.pop(vet)
        for vertex in self.__adj_list:
            if vet in self.__adj_list[vertex]:
                self.__adj_list[vertex].remove(vet)
