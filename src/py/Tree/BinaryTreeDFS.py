from utils.Node import TreeNode


class BinaryTreeDFS:
    def __init__(self):
        self.__result: list[TreeNode | None] = []


    def clear_result(self):
        self.__result = [None]


    # root -> left -> right
    def pre_order(self, root: TreeNode):
        if root is None:
            return
        self.__result.append(root)
        self.pre_order(root.left)
        self.pre_order(root.right)


    # left -> root -> right
    def in_order(self, root: TreeNode):
        if root is None:
            return
        self.in_order(root.left)
        self.__result.append(root)
        self.in_order(root.right)


    # left -> right -> root
    def post_order(self, root: TreeNode):
        if root is None:
            return
        self.post_order(root.left)
        self.post_order(root.right)
        self.__result.append(root)


    def get_result(self) -> list[TreeNode | None]:
        return self.__result
