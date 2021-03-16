class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def inorder(root, arr):
    if root == None:
        return

    inorder(root.left, arr)

    arr.append(root.key)

    inorder(root.right, arr)


def countNoes(root):
    if root == None:
        return 0

    return countNoes(root.left) + countNoes(root.right) + 1

def arrayToBST(arr, root):
    if root is None:
        return

    # first update the left tree
    arrayToBST(arr, root.left)

    #now update the root's data and delete the value from array
    root.key = arr[0]
    arr.pop(0)

    # updateh right tree
    arrayToBST(arr, root.right)


def binaryTree_to_BST(root):
    if root is None:
        return None

    n = countNoes(root)
    arr = []
    inorder(root, arr)

    arr.sort()

    arrayToBST(arr, root)

def printInorder(root):
    if root is None:
        return None

    printInorder(root.left)
    print(root.key)
    printInorder(root.right)


# Driver program to test above function
root = Node(10)
root.left = Node(30)
root.right = Node(15)
root.left.left = Node(20)
root.right.right = Node(5)

# Convert binary tree to BST
binaryTree_to_BST(root)

print("Following is the inorder traversal of the converted BST")
printInorder(root)