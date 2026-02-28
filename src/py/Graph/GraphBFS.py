from utils.Vertex import Vertex
from ListGraph import ListGraph
from Queue.ArrayQueue import ArrayQueue
from HashMap.HashSet import HashSet


def graph_bfs(graph: ListGraph, start_vet: Vertex) -> list[Vertex]:
    res = []
    visited = HashSet()
    que = ArrayQueue()

    visited.add(start_vet)
    que.pop(start_vet)
    while que.size() > 0:
        vet = que.pop()
        res.append(vet)
        for adj_vet in graph.__adj_list[vet]:
            if adj_vet in visited:
                continue
            que.push(adj_vet)
            visited.add(adj_vet)
    return res

