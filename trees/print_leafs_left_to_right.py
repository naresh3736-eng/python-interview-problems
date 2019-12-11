class node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

result = []
def print_leafs_left_to_right(root):
    if root is None:
        return None

    if root.left is None and root.right is None:
        result.append(root.key)

    if root.left != None:
        print_leafs_left_to_right(root.left)

    if root.right != None:
        print_leafs_left_to_right(root.right)

    return result

root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(5)

print print_leafs_left_to_right(root)


result = []
def print_leafs_right_to_left(root):
    if root is None:
        return None

    if root.left is None and root.right is None:
        result.append(root.key)

    if root.left != None:
        print_leafs_right_to_left(root.right)

    if root.right != None:
        print_leafs_right_to_left(root.left)

    return result

root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(5)

print print_leafs_right_to_left(root)


def print_leaft_ndoes_recustion(root):
    if root is None:
        return None

    if root.left is None and root.right is None:
        return root.key
    else:
        return str(print_leaft_ndoes_recustion(root.left)) + ',' +str(print_leaft_ndoes_recustion(root.right))

root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(5)

print print_leaft_ndoes_recustion(root)