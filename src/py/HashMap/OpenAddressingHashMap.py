import Hash
import HashMap


class OpenAddressingHashMap:
    def __init__(self):
        self.__size = 0
        self.__capacity = 50
        self.__thres = 2.0 / 3.0
        self.__ratio = 2
        self.__buckets: list[HashMap.Pair | None] = [None] * self.__capacity
        self.__TOMBSTONE = HashMap.Pair("TOMBSTONE", -1)

    
    def __hash(self, key) -> int:
        return Hash.mul_hash(key) % self.__capacity
    

    def __factor(self) -> float:
        return self.__size / self.__capacity
    

    def __find(self, key) -> int:
        index = self.__hash(key)
        tombstone_index = -1
        while self.__buckets[index] is not None:
            if self.__buckets[index].key == key:
                if tombstone_index != -1:
                    self.__buckets[tombstone_index] = self.__buckets[index]
                    self.__buckets[index] = self.__TOMBSTONE
                    return tombstone_index
                return index
            if tombstone_index == -1 and self.__buckets[index] is self.__TOMBSTONE:
                tombstone_index = index
            index = (index + 1) % self.__capacity
        return index if tombstone_index == -1 else tombstone_index
    

    def __extend(self):
        tmp = self.__buckets
        self.__capacity *= self.__ratio
        self.__buckets = [None] * self.__capacity
        self.__size = 0
        for i in tmp:
            if i not in [None, self.__TOMBSTONE]:
                self.put(i.key, i.val)


    def put(self, key, val):
        if self.__factor() > self.__thres:
            self.__extend()
        index = self.__find(key)
        if self.__buckets[index] not in [None, self.__TOMBSTONE]:
            self.__buckets[index].val = val
            return
        self.__buckets[index] = HashMap.Pair(key, val)
        self.__size += 1


    def get(self, key):
        index = self.__find(key)
        if self.__buckets[index] not in [None, self.__TOMBSTONE]:
            return self.__buckets[index].val
        return None
    

    def remove(self, key):
        index = self.__find(key)
        if self.__buckets[index] not in [None, self.__TOMBSTONE]:
            self.__buckets[index] = self.__TOMBSTONE
            self.__size -= 1


    def entrys(self, key) -> list[HashMap.Pair]:
        result: list[HashMap.Pair] = []
        for i in self.__buckets:
            if i not in [None, self.__TOMBSTONE]:
                result.append(i)
        return result

    
