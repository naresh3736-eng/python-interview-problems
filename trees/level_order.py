class node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def level_order(root):
    if root is None:
        return None
    queue = []
    queue.append(root)

    while len(queue) >= 1:
        node = queue.pop(0)
        print node.key

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(5)
root.right.left = node(6)
root.right.right = node(7)

level_order(root)