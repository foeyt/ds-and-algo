class ArrayQueue:
    def __init__(self):
        self.__li: list = []
        self.__front: int = 0
        self.__size: int = 0

    
    def size(self):
        return self.__size
    
    
    def push(self, val):
        capacity = len(self.__li)
        if self.__size >= capacity:
            raise IndexError
        rear = (self.__front + self.__size) % capacity
        self.__li[rear] = val
        self.__size += 1


    def pop(self):
        capacity = len(self.__li)
        val = self.__li[self.__front]
        self.__front = (self.__front + 1) % capacity
        self.__size -= 1
        return val
    

    def access(self) -> int:
        return self.__li[self.__front]
    
    
    def to_list(self) -> list:
        li: list = []
        j = self.__front
        capacity = len(self.__li)
        for i in range(0, self.__size):
            li[i] = self.__li[j % capacity]
            j += 1
        return li

