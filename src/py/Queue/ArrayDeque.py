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


    def __push_tail(self, val):
        capacity = len(self.__li)
        if self.__size >= capacity:
            raise IndexError
        else:
            rear = self.__index(self.__front + self.__size + 1)
            self.__li[rear] = val
        self.__size += 1


    def __pop_head(self):
        val = self.__li[self.__front]
        self.__front = self.__index(self.__front + 1)
        self.__size -= 1
        return val
    

    def __pop_tail(self):
        rear = self.__index(self.__front + self.__size)
        val = self.__li[rear]
        self.__size -= 1
        return val
    

    def __access_head(self):
        return self.__li[self.__front]
    

    def __access_tail(self):
        return self.__li[self.__index(self.__index + self.__size)]


    def push(self, val, mode="tail"):
        if mode == "tail":
            self.__push_tail(val)
        elif mode == "head":
            self.__push_head(val)
        else:
            raise TypeError
        

    def pop(self, mode="head"):
        if mode == "head":
            self.__pop_head()
        elif mode == "tail":
            self.__pop_tail()
        else:
            raise TypeError
        

    def access(self, mode="head"):
        if mode == "head":
            self.__access_head()
        elif mode == "tail":
            self.__access_tail()
        else:
            raise TypeError
        

    def to_list(self) -> list:
        li: list = []
        j = self.__front
        for i in range(0, self.__size):
            li[i] = self.__li[self.__index(j)]
            j += 1
        return li

