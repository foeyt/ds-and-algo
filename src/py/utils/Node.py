class LinkedNode:
    def __init__(self, val):
        self.val = val
        self.next: LinkedNode | None = None

class DoubleLinkedNode:
    def __init__(self, val):
        self.val = val
        self.prev: DoubleLinkedNode | None = None
        self.next: DoubleLinkedNode | None = None


class TreeNode:
    def __init(self, val):
        self.val = val
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None
