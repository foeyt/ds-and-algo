class AVLTreeNode:
    def __init__(self, val):
        self.val = val
        self.height: int = 0
        self.left: AVLTreeNode | None = None
        self.right: AVLTreeNode | None = None


def height(node: AVLTreeNode | None) -> int:
    return node.height if node is not None else -1


def update_height(node: AVLTreeNode | None):
    node.height = max(height(node.left), height(node.right)) + 1


def factor(node: AVLTreeNode | None) -> int:
    return node.left.height - node.right.height if node is not None else 0


def right_rotate(node: AVLTreeNode | None) -> AVLTreeNode | None:
    child = node.left
    grand_child = child.right
    child.right = node
    node.left = grand_child
    update_height(node)
    update_height(child)
    return child


def left_rotate(node: AVLTreeNode | None) -> AVLTreeNode | None:
    child = node.right
    grand_child = child.left
    child.left = node
    node.right = grand_child
    update_height(node)
    update_height(child)
    return child


def rotate(node: AVLTreeNode | None) -> AVLTreeNode | None:
    fac = factor(node)
    if fac > 1:
        if factor(node.left) >= 0:
            return right_rotate(node)
        else:
            node.left = left_rotate(node.left)
            return right_rotate(node)
    elif fac < -1:
        if factor(node.right) <= 0:
            return left_rotate(node)
        else:
            node.right = right_rotate(node.right)
            return left_rotate(node)
    return node


def insert_helper(node: AVLTreeNode | None, val) -> AVLTreeNode | None:
    if node is None:
        return AVLTreeNode(val)
    if node.val < val:
        node.right = insert_helper(node.right, val)
    elif node.val > val:
        node.left = insert_helper(node.left, val)
    else:
        return node
    update_height(node)
    return rotate(node)


def remove_helper(node: AVLTreeNode | None, val) -> AVLTreeNode | None:
    if node is None:
        return None
    if node.val < val:
        node.right = remove_helper(node.right, val)
    elif node.val > val:
        node.left = remove_helper(node.left, val)
    else:
        if node.left is None or node.right is None:
            child = node.left or node.right
            if child is None:
                return None
            else:
                node = child
        else:
            tmp = node.right
            while tmp.left is not None:
                tmp = tmp.left
            node.right = remove_helper(node.right, val)
            node.val = tmp.val
    update_height(node)
    return rotate(node)


def insert(root: AVLTreeNode | None, val):
    root = insert_helper(root, val)


def root(root: AVLTreeNode | None, val):
    root = remove_helper(root, val)


def search(root: AVLTreeNode | None, val) -> AVLTreeNode | None:
    if root is None:
        return None
    cur = root
    while cur.val != val:
        if cur.val < val:
            cur = cur.right
        elif cur.val > val:
            cur = cur.left
        else:
            break
    return cur
