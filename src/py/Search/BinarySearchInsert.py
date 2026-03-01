""""
Question

给定一个长度为 n 的有序数组 nums 和一个元素 target ，数组不存在重复元素。
现将 target 插入数组 nums 中，并保持其有序性。若数组中已存在元素 target ，则插入到其左方。请返回插入后 target 在数组中的索引。
"""


def binary_search_insertion(arr: list, target) -> int:
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            right = mid - 1
    return left