import Hash


class HashSet:
    def __init__(self):
        self.__capacity = 100
        self.__buckets = [[] for _ in range(self.__capacity)]


    def __hash(self, key) -> int:
        return Hash.mul_hash(key) % self.__capacity
    

    def add(self, val):
        index = self.__hash(val)
        if val not in self.__buckets:
            self.__buckets[index].append(val)


    def remove(self, val):
        index  = self.__hash(val)
        if val in self.__buckets:
            self.__buckets[index].remove(val)


    def contains(self, val) -> bool:
        index = self.__hash(val)
        return val in self.__buckets[index]
