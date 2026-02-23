from utils.Node import LinkedNode

class LinkedQueue:
    def __init__(self):
        self.__head: LinkedNode | None = None
        self.__tail: LinkedNode | None = None
        self.__size: int = 0


    def size(self):
        return self.__size
    
    
    def push(self, val):
        node = LinkedNode(val)
        if self.__head is None:
            self.__head = self.__tail = node
        else:
            if self.__tail is None:
                self.__tail = node
            else:
                self.__tail.next = node
                self.__tail = node
        self.__size += 1


    def pop(self):
        node = self.__head
        self.__head = node.next
        node.next = None
        return node.val
    

    def access(self):
        return self.__head.val
    

    def to_list(self) -> list:
        li: list = []
        p = self.__head
        while p is not None:
            li.append(p.val)
            p = p.next

        return li
