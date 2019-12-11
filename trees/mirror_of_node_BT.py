class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def findMirrorRec(target, left, right):
    if left == None or right == None:
        return None

    if left.data == target:
        return right.data
    if right.data == target:
        return left.data

    mirror_val = findMirrorRec(target, left.left, right.right)
    if mirror_val != None:
        return mirror_val

    findMirrorRec(target, left.right, right.left)

def findMirror(root, target):
    if root == None:
        return None

    if root.data == target:
        return target

    return findMirrorRec(target, root.left, root.right)