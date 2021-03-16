class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def mirror(root):
    if root == None:
        return None

    mirror(root.left)
    mirror(root.right)

    temp = root.left
    root.left = root.right
    root.right = temp

def inorder(root):
    if root == None:
        return None

    inorder(root.left)
    print(root.data)
    inorder(root.right)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Inorder traversal before mirror")
    inorder(root)

    mirror(root)

    print("Inorder traversal after mirror")
    inorder(root)