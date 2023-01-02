class Tree:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val
class Solution:
    def height(self, root):
        if not root:
            return 0

        l_height = self.height(root.left)
        r_height = self.height(root.right)

        return max(int(l_height), int(r_height)) + 1


ro = Tree(1)

