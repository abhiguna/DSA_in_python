from BinaryTreeNode import BinaryTreeNode
from BinaryTree import BinaryTree

class InorderIterator:
    def __init__(self, root):
        self.stack = []
        self.populate_ierator(root)

    def populate_iterator(self, root):
        while not root:
            self.stack.append(root)
            root = root.left

    def hasNext(self):
        if not self.stack:
            return False
        return True

    def getNext(self):
        if not self.stack:
            return None
        ret_val = self.stack[-1]
        del self.stack[-1]

        temp = ret_val.right
        self.populate_iterator(temp)
        return ret_val


