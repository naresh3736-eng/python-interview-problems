'''
given a tree, minVal and maxval, trim a bst in such a way that it contains nodes in between minVal and maxVal and shoiuld be a binary tree
'''

def trimBST(tree, minVal, maxVal):
    tree.left = trimBST(tree.left, minVal, maxVal)
    tree.right = trimBST(tree.right, minVal, maxVal)

    if minVal <= tree.key <= maxVal:
        return tree

    if minVal < tree.key:
        return tree.right

    if maxVal > tree.key:
        return tree.left