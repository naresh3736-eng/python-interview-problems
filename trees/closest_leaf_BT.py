class newNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def findLeafDown(root, lev, minDist):
    if root is None:
        return

# if this is the leaf node then check if this is the closer than the closest so far
    if root.left == None and root.right == None:
        if lev < minDist[0]:
            minDist[0] = lev
        return

# check in right and left subtrees
    findLeafDown(root.left, lev+1, minDist)
    findLeafDown(root.right, lev+1, minDist)


def findThroughParent(root, x, minDist):
    if root is None:
        return -1

    if root == x:
        return 0

    l = findThroughParent(root.left, x, minDist)

    if l != -1:
        findLeafDown(root.right, l+2, minDist)
        return l + 1

    r = findThroughParent(root.right, x, minDist)
    if r!= -1:
        findLeafDown(root.left, r+2, minDist)
        return r + 1

    return -1

def minimumDistance(root, x):
    minDist = [999999999999]

    findLeafDown(x, 0, minDist)

    findThroughParent(root, x, minDist)

    return minDist[0]


if __name__ == '__main__':
    # Let us create Binary Tree shown
    # in above example

    root = newNode(1)
    root.left = newNode(12)
    root.right = newNode(13)

    root.right.left = newNode(14)
    root.right.right = newNode(15)

    root.right.left.left = newNode(21)
    root.right.left.right = newNode(22)
    root.right.right.left = newNode(23)
    root.right.right.right = newNode(24)

    root.right.left.left.left = newNode(1)
    root.right.left.left.right = newNode(2)
    root.right.left.right.left = newNode(3)
    root.right.left.right.right = newNode(4)
    root.right.right.left.left = newNode(5)
    root.right.right.left.right = newNode(6)
    root.right.right.right.left = newNode(7)
    root.right.right.right.right = newNode(8)

    x = root.right

    print("The closest leaf to the node with value",
          x.key, "is at a distance of",
          minimumDistance(root, x))