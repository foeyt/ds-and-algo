from ListGraph import ListGraph
from HashMap.HashSet import HashSet
from utils.Vertex import Vertex


def dfs(graph: ListGraph, visited: HashSet, res: list[Vertex], vet: Vertex):
    res.append(vet)
    visited.add(vet)
    for adj_vet in graph.__adj_list[vet]:
        if adj_vet in visited:
            continue
        dfs(graph, visited, res, vet)


def graph_dfs(graph: ListGraph, start_vet: Vertex) -> list[Vertex]:
    res = []
    visited = HashSet()
    dfs(graph, visited, res, start_vet)
    return res
