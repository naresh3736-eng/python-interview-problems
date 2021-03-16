class node:
    def __init__(self, key):
        self.key = key
        self.leftchild = None
        self.rightchild = None

def generate_ancestors(root, ancestors):
    ancestors[root.key] = -1

    queue = []
    queue.append(root)

    while len(queue) >= 1:
        node = queue[0]
        queue.pop(0)

        if node.leftchild:
            ancestors[node.leftchild.key] = node.key
            queue.append(node.leftchild)

        if node.rightchild:
            ancestors[node.rightchild.key] = node.key
            queue.append(node.rightchild)


def find_kth_ancestor(root, n, k, node):
    ancestors = [0] * (n+1)

    generate_ancestors(root, ancestors)

    print(ancestors)

    count = 0

    while node != -1:
        node = ancestors[node]
        count += 1

        if count == k:
            break
    return node

root = node(1)
root.leftchild = node(2)
root.rightchild = node(3)
root.leftchild.leftchild = node(4)
root.leftchild.rightchild = node(5)

k = 2
node = 5

print(find_kth_ancestor(root, 5, k, node))
