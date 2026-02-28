class MatrixGraph:
    def __init__(self, __verticles: list, edges: list[list[int]]):
        self.__verticles: list = []
        self.__adj_mat: list[list[int]] = []
        for val in __verticles:
            self.add_vertix(val)
        for e in edges:
            self.add_edge(e[0], e[1])


    def size(self) -> int:
        return len(self.__verticles)
    

    def add_vertix(self, val):
        n = self.size()
        self.__verticles.append(val)
        new_row = [0] * n
        self.__adj_mat(new_row)
        for row in self.__adj_mat:
            row.append(0)


    def remove_vertix(self, index: int):
        if index >= self.size():
            raise IndexError
        self.__verticles.pop(index)
        self.__adj_mat.pop(index)
        for row in self.__adj_mat:
            row.pop(index)


    def add_edge(self, i: int, j: int):
        if i < 0 or j < 0 and i >= self.size() or j >= self.size() or i == j:
            raise IndexError
        self.__adj_mat[i][j] = 1
        self.__adj_mat[j][i] = 1


    def remove_edge(self, i: int, j: int):
        if i < 0 or j < 0 and i >= self.size() or j >= self.size() or i == j:
            raise IndexError
        self.__adj_mat[i][j] = 0
        self.__adj_mat[j][i] = 0


    def get_verticles(self) -> list:
        return self.__verticles
    

    def get_edges(self) -> list[list[int]]:
        return self.__adj_mat
