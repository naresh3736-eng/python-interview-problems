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
        print(temp.data, end='->')

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

# leetcode to print the nodes in sub lists e.g. Input: root = [3,9,20,null,null,15,7] Output: [[3],[20,9],[15,7]]

def leetcodeProblem(root: Node):
    if root is None:
        return []
    current_val = []
    next_val = []
    result = []
    left_to_right = True
    current_val.append(root)
    while len(current_val) > 0:
        temp = []
        #print(curr.data, end='->')
        size = len(current_val)
        while size != 0:
            curr = current_val.pop()
            temp.append(curr.data)
            if left_to_right:
                if curr.left:
                    next_val.append(curr.left)
                if root.right:
                    next_val.append(root.right)
            else:
                if curr.right:
                    next_val.append(curr.right)
                if curr.left:
                    next_val.append(curr.left)
            size -= 1

        if len(current_val) == 0:
            left_to_right = False
            current_val, next_val = next_val, current_val
        result.append(temp)
    print(result)

root1 = Node(1)
print('\n')
leetcodeProblem(root1)