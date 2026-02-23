from utils.Node import TreeNode
from Stack.LinkedStack import LinkedStack

class BinarySearchTree:
    def __init__(self):
        self.__root: TreeNode | None = None


    def get_root(self) -> TreeNode | None:
        return self.__root
    

    def search(self, val) -> TreeNode | None:
        cur: TreeNode | None = self.__root
        while cur.val != val:
            if cur.val < val:
                cur = cur.right
            elif cur.val > val:
                cur = cur.left
            else:
                break
        return cur
    

    def insert(self, val):
        if self.__root is None:
            self.__root = TreeNode(val)
            return
        cur, pre = self.__root, None
        while cur is not None:
            if cur.val == val:
                return
            pre = cur
            if cur.val < val:
                cur = cur.right
            elif cur.val > val:
                cur = cur.left
        node = TreeNode(val)
        if pre.val < val:
            pre.right = node
        elif pre.val > val:
            pre.left = node


    def remove(self, val):
        if self.__root is None:
            return
        cur, pre =  self.__root, None
        while cur is not None:
            if cur.val == val:
                return
            pre = cur
            if cur.val < val:
                cur = cur.right
            elif cur.val > val:
                cur = cur.left
        if cur is None:
            return
        if cur.left is None or cur.right is None:
            child = cur.left or cur.right
            if cur != self.__root:
                if pre.left == cur:
                    pre.left= child
                else:
                    pre.right = child
            else:
                self.__root = child
        else:
            tmp: TreeNode = cur.right
            while tmp.left is not None:
                tmp = tmp.left
            self.remove(tmp.val)
            cur.val = tmp.val


    def in_order(self) -> list:
        result: list = []
        stack: LinkedStack = LinkedStack()
        tmp: TreeNode = self.__root
        while tmp or stack:
            while tmp is not None:
                stack.push(tmp.val)
                tmp = tmp.left
            tmp = stack.pop()
            result.append(tmp.val)
            tmp = tmp.right
        return result
