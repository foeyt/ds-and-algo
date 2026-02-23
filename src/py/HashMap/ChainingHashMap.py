import Hash
import HashMap


class ChainingHashMap:
    def __init__(self):
        self.__size = 0
        self.__capacity = 50
        self.__thres = 2.0 / 3.0
        self.__ratio = 2
        self.__buckets = [[] for _ in range(self.__capacity)]


    def __hash(self, key) -> int:
        return Hash.mul_hash(key) % self.__capacity
    

    def __factor(self) -> float:
        return self.__size / self.__capacity
    

    def __extend(self):
        buckets = self.__buckets
        self.__capacity *= self.__ratio
        self.__buckets = [[] for _ in range(self.__capacity)]
        self.__size = 0
        index = 0
        for i in buckets:
            self.__buckets[index] = i
            index += 1


    def put(self, key, val):
        if self.__factor() > self.__thres:
            self.__extend()
        bucket: list[HashMap.Pair | None] = self.__buckets[self.__hash(key)]
        for i in bucket:
            if i.key == key:
                i = HashMap.Pair(key, val)
                return
        pair = HashMap.Pair(key, val)
        bucket.append(pair)
        self.__size += 1


    def get(self, key):
        bucket: list[HashMap.Pair | None] = self.__buckets[self.__hash(key)]
        for i in bucket:
            if i.key == key:
                return i.val
        return None
    

    def remove(self, key):
        bucket: list[HashMap.Pair | None] = self.__buckets[self.__hash(key)]
        for i in bucket:
            if i.key == key:
                bucket.remove(i)
                self.__size -= 1
                break


    def entrys(self, key) -> list[HashMap.Pair]:
        result: list[HashMap.Pair] = []
        for i in self.__buckets:
            for j in i:
                if j is not None:
                    result.append(j)
        return result
