"""
Question

给定一个整数数组 nums 和一个目标元素 target ，请在数组中搜索“和”为 target 的两个元素，并返回它们的数组索引。返回任意一个解即可。
"""


def two_sum_brute_force(arr: list, target) -> list[int]:
    for i in range(len(arr) - 1):
        for j in range(i, len(arr)):
            if arr[i] + arr[j] == target:
                return [i, j]
    return []


def two_sum_hash(arr: list, target) -> list[int]:
    dic = {}
    for i in range(len(arr)):
        if target - arr[i] in dic:
            return [dic[target - arr[i]], i]
        dic[arr[i]] = i
    return -1
