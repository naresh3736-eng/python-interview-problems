class TreeNode:
    def __init__(self, val):
        self.data = val
        self.left = self.right = None

def diameterOfBT(root: TreeNode) -> int:
    if root is None:
        return 0
    leftheight = height(root.left)
    rightheight = height(root.right)

    leftdiameter = diameterOfBT(root.left)
    rightdiameter = diameterOfBT(root.right)

    return max(leftheight+rightheight, max(leftdiameter, rightdiameter))

def height(root: TreeNode) -> int:
    if root is None:
        return 0
    else:
        return 1 + max(height(root.left), height(root.right))

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(3)

print(diameterOfBT(root))