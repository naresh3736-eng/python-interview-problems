class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def hasPath(root, x, arr):
    if root is None:
        return None

    arr.append(root.data)

    if root == x:
        return True

    if hasPath(root.left, x, arr) or hasPath(root.right, x, arr):
        return True

    arr.pop(-1)

    return False


def printPath(root, x):
    arr = []

    if hasPath(root, x, arr):
        for i in range(len(arr)-1):
            #print(arr[i], end="==>")
            print arr[i]
        print()

    else:
        print("No path")


if __name__ == '__main__':
    # binary tree formation
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    x = 5
    printPath(root, x)

