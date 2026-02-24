from Heap import Heap


def topk(arr: list, k: int) -> list:
    heap: Heap = Heap([])
    for i in range(k):
        heap.push(arr[i])
    for i in range(k, len(arr)):
        if arr[i] > heap[0]:
            heap.pop()
            heap.push(arr[i])
    return heap
