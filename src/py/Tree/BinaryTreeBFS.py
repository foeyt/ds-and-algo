from utils.Node import TreeNode
from Queue.ArrayQueue import ArrayQueue

def level_order(root: TreeNode) -> list[TreeNode]:
    queue: ArrayQueue = ArrayQueue()
    queue.push(root)
    result: list[TreeNode] = []
    while queue.size != 0:
        node: TreeNode = queue.pop()
        result.append(node)
        if node.left is not None:
            queue.push(node.left)
        elif node.right is not None:
            queue.push(node.right)
    return result
    