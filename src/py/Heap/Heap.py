class Heap:
    def __init__(self, arr: list):
        self.__heap: list = list(arr)
        for i in range((self.size() - 1), -1, -1):
            self.__sift_down(i)

    
    def left(self, index: int) -> int:
        return 2 * index + 1
    

    def right(self, index: int) -> int:
        return 2 * index + 2
    

    def parent(self, index: int) -> int:
        return (index - 1) // 2


    def peek(self):
        return self.__heap[0]
    

    def size(self):
        return len(self.__heap)
    

    def __sift_up(self, index: int):
        while True:
            p = self.parent(index)
            if p < 0 or self.__heap[index] <= self.__heap[p]:
                break
            self.__heap[index], self.__heap[p] = self.__heap[p], self.__heap[index]
            index = p

    def push(self, val):
        self.__heap.append(val)
        self.__sift_up(self.size() - 1)


    def __sift_down(self, index: int):
        while True:
            l, r, m = self.left(index), self.right(index), index
            if l < self.size() and self.__heap[l] > self.__heap[m]:
                m = l
            if r < self.size() and self.__heap[r] > self.__heap[m]:
                m = r
            if m == index:
                break
            self.__heap[index], self.__heap[m] = self.__heap[m], self.__heap[index]
            index = m


    def pop(self):
        if self.size() == 0:
            raise IndexError
        self.__heap[0], self.__heap[self.size() - 1] = self.__heap[self.size() - 1], self.__heap[0]
        val = self.__heap[0]
        self.__sift_down(0)
        return val
