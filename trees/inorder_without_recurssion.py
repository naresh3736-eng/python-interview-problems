class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

def inorderWithourRecurssion(root):
    if root is None:
        return
    current = root
    stack = []

    while True:
        if current is not None:
            stack.append(current)
            current = current.left
        elif(stack):
            current = stack.pop()
            print(current.data, end=" ")
            current = current.right
        else:
            break

