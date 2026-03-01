"""
选择排序：
时间复杂度： O(n^2)
空间复杂度： O(1)
稳定性：不稳定
"""
def selection_sort(arr: list[int]):
    n = len(arr)
    for i in range(n - 1):
        k = i
        for j in range(i + 1, n):
            if arr[j] < arr[k]:
                k = j
        arr[i], arr[k] = arr[k], arr[i]


"""
冒泡排序：
时间复杂度：O(n) 至 O(n^2)
空间复杂度：O(1)
稳定性：稳定
"""
def bubble_sort(arr: list[int]):
    n = len(arr)
    for i in range(n - 1, 0, -1):
        flag = False
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = True
        if not flag:
            break



"""
插入排序：
时间复杂度：O(n) 至 O(n^2)
空间复杂度：O(1)
稳定性：稳定
其他性质：自适应
"""
def insertion_sort(arr: list[int]):
    n = len(arr)
    for i in range(1, n):
        base = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > base:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = base


"""
快速排序：

"""
def __partition(arr: list, left: int, right: int) -> int:
    i, j = left, right
    while i < j:
        while i < j and arr[j] >= arr[left]:
            j -= 1
        while i < j and arr[i] <= arr[left]:
            i += 1
        arr[i], arr[j] = arr[j], arr[i]
    arr[left], arr[i] = arr[i], arr[left]
    return i


def quick_sort(arr: list, left: int, right: int):
    if left >= right:
        return
    pivot = __partition(arr, left, right)
    quick_sort(arr, left, pivot - 1)
    quick_sort(arr, pivot + 1, right)

