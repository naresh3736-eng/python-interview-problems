class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

def zigzag(root):
    if root is None:
        return None

    current_value = []
    next_value = []

    left_to_right = True

    current_value.append(root)

    while len(current_value) > 0:
        temp = current_value.pop()
        print(temp.data)

        if left_to_right:
            if temp.left:
                next_value.append(temp.left)
            if temp.right:
                next_value.append(temp.right)
        else:
            if temp.right:
                next_value.append(temp.right)
            if temp.left:
                next_value.append(temp.left)

        if len(current_value) == 0:
            left_to_right = False
            current_value, next_value = next_value, current_value


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(7)
root.left.right = Node(6)
root.right.left = Node(5)
root.right.right = Node(4)
print("Zigzag Order traversal of binary tree is")
zigzag(root)