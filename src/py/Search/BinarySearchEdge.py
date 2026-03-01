"""
Question

给定一个长度为 n 的有序数组 nums ，其中可能包含重复元素。请返回数组中最左一个元素 target 的索引。若数组中不包含该元素，则返回 -1。
"""


import BinarySearchInsert


def binary_search_left_edge(arr: list, target) -> int:
    i = BinarySearchInsert.binary_search_insertion(arr, target)
    if i == len(arr) or arr[i] != target:
        return -1
    return i


def binary_search_right_edge(arr: list, target) -> int:
    i = BinarySearchInsert.binary_search_insertion(arr, target + 1)
    j = i - 1
    if j == -1 or arr[j] != -1:
        return -1
    return j
