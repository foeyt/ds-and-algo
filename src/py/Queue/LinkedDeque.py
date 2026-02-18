import utils.Node as Utils

class LinkedDeque:
    def __init__(self):
        self.__head: Utils.DoubleLinkedNode | None = None
        self.__tail: Utils.DoubleLinkedNode | None = None
        self.__size: int = 0


    def size(self):
        return self.__size
    

    def __push_head(self, val):
        node = Utils.DoubleLinkedNode(val)
        if self.__size == 0:
            self.__head = self.__tail = node
        else:
            node.next = self.__head
            self.__head.prev = node
            self.__head = node
        self.__size += 1


    def __push_tail(self, val):
        node = Utils.DoubleLinkedNode(val)
        if self.__size == 0:
            self.__head = self.__tail = node
        else:
            node.prev = self.__tail
            self.__tail.next = node
            self.__tail = node
        self.__size += 1


    def __pop_head(self):
        node = self.__head
        self.__head = node.next
        node.next = None
        self.__head = None
        self.__size -= 1
        return node.val
    

    def __pop_tail(self):
        node = self.__tail
        self.__tail = node.prev
        node.prev = None
        self.__tail.next = None
        self.__size -= 1
        return node.val
    

    def __access_head(self):
        return self.__head.val
    

    def __access_tail(self):
        return self.__tail.val
    

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
        p = self.__head
        while p is not None:
            li.append(p.val)
            p = p.next
        return li
