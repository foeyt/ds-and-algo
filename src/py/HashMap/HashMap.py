import Hash


class Pair:
    def __init__(self, key, val):
        self.key = key
        self.val = val

    def format(self) -> str:
        return self.key + " -> " + self.val


class HashMap:
    def __init__(self):
        self.__capacity: int = 100
        self.__size: int = 0
        self.__buckets: list[Pair | None] = [None] * self.__capacity


    def __hash(self, key) -> int:
        return Hash.mul_hash(key) % self.__capacity
    
    
    def size(self):
        return self.__size
    

    def put(self, key, val):
        if self.__capacity <= self.__size:
            self.__extend()

        pair: Pair = Pair(key, val)
        self.__buckets[self.__hash(key)] = pair
        self.__size += 1


    def get(self, key):
        pair: Pair = self.__buckets[self.__hash(key)]
        return pair.val if pair is not None else None
    

    def remove(self, key):
        self.__buckets[self.__hash(key)] = None
        self.__size -= 1


    def entrys(self) -> list[Pair]:
        result: list[Pair] = []
        for i in self.__buckets:
            if i is None:
                continue
            result.append(i)
        return result
    

    def __extend(self):
        self.__capacity *= 2
        new_buckets: list[Pair | None] = [None] * self.__capacity
        index: int = 0
        for i in self.__buckets:
            new_buckets[index] = i
            index += 1

        self.__buckets = new_buckets
