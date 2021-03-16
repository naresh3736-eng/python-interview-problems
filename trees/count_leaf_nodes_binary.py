class node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def count_leaf_nodes_recursive(root):
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return 1
    else:
        count = count_leaf_nodes_recursive(root.left) + count_leaf_nodes_recursive(root.right)
        return count


root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(5)

print(count_leaf_nodes_recursive(root))


def count_leaf_nodes_iterative(root):
    if root is None:
        return 0
    queue = []
    queue.append(root)
    count = 0

    while len(queue) >= 1:
        node = queue[0]
        queue.pop(0)

        if (node.left == None) and (node.right == None):
            count +=1
        else:
            queue.append(node.left)
            queue.append(node.right)

    return count

root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(5)

print(count_leaf_nodes_iterative(root))
