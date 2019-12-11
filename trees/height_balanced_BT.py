class node:
    def __init__(self, key):
        self.key = key
        self.leftcihld = None
        self.rightchild = None


def height(root, current_height):
    if root == None:
        return current_height

    else:
        left_height = height(root.leftchild, current_height+1)
        right_child = height(root.rightchild, current_height+1)

        return (left_height-right_child) <=1


