import utils.Node as Utils

class LinkedStack:
    def __init__(self):
        self.__peek: Utils.LinkedNode | None = None
        self.__size: int = 0


    def size(self):
        return self.__size
    

    def access(self):
        return self.__peek.val
    

    def push(self, val):
        node = Utils.LinkedNode(val)
        node.next = self.__peek
        self.__peek = node
        self.__size += 1

    
    def pop(self):
        node = self.__peek
        self.__peek = node.next
        self.__size -= 1
        return node.val
    

    def to_list(self) -> list:
        li: list = []
        p = self.__peek
        while p is not None:
            li.append(p.val)
            p = p.next

        return li
