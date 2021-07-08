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
        print(node.key, end='->')

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

# leetcode problem level order to print nodes as lists e.g. Input: root = [3,9,20,null,null,15,7] Output: [[3],[9,20],[15,7]]

def leetcodeProblem(root: node):
    if root is None:
        return []
    result = []
    queue = []
    queue.append(root)
    while len(queue) > 0:
        temp = []
        size = len(queue)
        while size != 0:
            curr = queue.pop(0)
            temp.append(curr.key)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
            size -= 1
        result.append(temp)
    return result

print('\n', leetcodeProblem(root))