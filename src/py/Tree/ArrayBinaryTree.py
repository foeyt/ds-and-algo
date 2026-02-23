class ArrayBinaryTree:
    def __init__(self, arr: list):
        self.__tree: list = list(arr)
        self.__result: list = []


    def size(self):
        return len(self.__tree)
    

    def get(self, index: int):
        if index < 0 or index >= self.size():
            return None
        return self.__tree[index]
    

    def left(self, index: int) -> int | None:
        left: int = 2 * index + 1
        return left if left >= 0 and left < self.size() - 1 else None
    
    
    def right(self, index: int) -> int | None:
        right: int = 2 * index + 2
        return right if right >= 0 and right < self.size() - 1 else None


    def parent(self, index: int) -> int | None:
        parent: int = (index - 1) // 2
        return parent if parent >= 0 and parent < self.size() - 1 else None


    def level_order(self):
        self.__result: list = []
        for i in self.__tree:
            if i is not None:
                self.__result.append(i)
    

    def pre_order(self, index: int):
        if self.__tree[index] is None:
            return
        self.__result.append(self.__tree[index])
        self.pre_order(self.left(index))
        self.pre_order(self.right(index))
        
    
    def in_order(self, index: int):
        if self.__tree[index] is None:
            return      
        self.in_order(self.left(index))
        self.__result.append(self.__tree[index])
        self.in_order(self.right(index))


    def post_order(self, index: int):
        if self.__tree[index] is None:
            return
        self.post_order(self.left(index))
        self.post_order(self.right(index))
        self.__result.append(self.__tree[index])   


    def get_result(self) -> list:
        return self.__result
        
