from utils.Node import TreeNode


def insert(node: TreeNode, next: TreeNode, mode: str):
    if mode == "left":
        next.left = node.left
        node.left = next
    elif mode == "right":
        next.right = node.right
        node.right = next


def remove(node: TreeNode, mode: str):
    if mode == "left":
        node.left.left = node.left
    elif mode == "right":
        node.right.right = node.right
