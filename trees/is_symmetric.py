'''
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
'''

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

def isSymmetric(root: TreeNode):
    if root is None:
        return True
    return isMirror(root.left, root.right)

def isMirror(left: TreeNode, right: TreeNode):
    if left and right:
        return left.val == right.val and isMirror(left.left, right.right) and isMirror(left.right, right.left)
    return left == right