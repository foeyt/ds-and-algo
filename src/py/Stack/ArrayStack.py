import utils.Node as Utils

class ArrayStack:
    def __init__(self):
        self.__li: list = []

    
    def size(self):
        return len(self.__li)
    

    def access(self):
        return self.li[self.size() - 1]
    

    def push(self, val):
        self.__li.append(val)


    def pop(self):
        return self.__li.pop()


    def to_lit(self) -> list:
        return self.__li
