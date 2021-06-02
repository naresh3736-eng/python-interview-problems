class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

def preorderWithourRecurssion(root):
    if root is None:
        return
    stack = []
    stack.append(root)

    while len(stack) > 0:
        node = stack.pop()
        print(node.data, end=" ")
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)