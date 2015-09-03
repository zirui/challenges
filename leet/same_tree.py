

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def is_same_tree(self, p, q):
        if p is None or q is None:
            if p != q:
                return False
            return True
        if p.val != q.val:
            return False
        if not self.is_same_tree(p.left, q.left):
            return False
        return self.is_same_tree(p.right, q.right)
