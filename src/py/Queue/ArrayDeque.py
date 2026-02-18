class ArrayDeque:
    def __init__(self):
        self.__li: list = []
        self.__front: int = 0
        self.__size: int = 0


    def size(self):
        return self.__size
    

    def __index(self, i: int) -> int:
        capacity = len(self.__li)
        return (i + capacity) % capacity


    def __push_head(self, val):
        capacity = len(self.__li)
        if self.__size >= capacity:
            raise IndexError
        else:
            self.__front = self.__index(self.__front - 1)
            self.__li[self.__front] = val
        self.__size += 1

