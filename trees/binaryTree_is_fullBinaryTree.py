class Node:
    def __init__(self, key):
        self.key = key
        self.leftchild = None
        self.rightchild = None


# using recursion

def isFullBT_recursion(root):
    if root is None:
        return None

    if root.leftchild is None and root.rightchild is None:
        return True

    if root.leftchild is not None and root.rightchild is not None:
        return isFullBT_recursion(root.leftchild) and isFullBT_recursion(root.rightchild)

    return False

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.right = Node(40);
root.left.left = Node(50);
root.right.left = Node(60);
root.right.right = Node(70);

root.left.left.left = Node(80);
root.left.left.right = Node(90);
root.left.right.left = Node(80);
root.left.right.right = Node(90);
root.right.left.left = Node(80);
root.right.left.right = Node(90);
root.right.right.left = Node(80);
root.right.right.right = Node(90);

if isFullBT_recursion(root):
    print "The Binary tree is full"
else:
    print "Binary tree is not full"


# using iterative approach

def isFullBT_iterative(root):
    if root is None:
        return None

    queue = []
    queue.append(root)

    while len(queue) >=1:
        node = queue[0]
        queue.pop(0)

        if node.leftchild is None and node.rightchild is None:
            continue

        if node.leftchild is not None or node.rightchild is not None:
            return False

        queue.append(node.leftchild)
        queue.append(node.rightchild)

    return True

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.right = Node(40);
root.left.left = Node(50);
root.right.left = Node(60);
root.right.right = Node(70);

root.left.left.left = Node(80);
root.left.left.right = Node(90);
root.left.right.left = Node(80);
root.left.right.right = Node(90);
root.right.left.left = Node(80);
root.right.left.right = Node(90);
root.right.right.left = Node(80);
root.right.right.right = Node(90);

if isFullBT_iterative(root):
    print "The Binary tree is full"
else:
    print "Binary tree is not full"