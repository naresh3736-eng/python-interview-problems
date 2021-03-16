class Node():
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None

class BST():
    def __init__(self):
        self.root = None

    # insertion part
    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, current_node):
        if value < current_node.value:
            if current_node.left_child == None:
                current_node.left_child = Node(value)
            else:
                self._insert(value, current_node.left_child)

        elif value > current_node.value:
            if current_node.right_child == None:
                current_node.right_child = Node(value)
            else:
                self._insert(value, current_node.right_child)

        else:
            print('value already exists')


    # height of a tree

    def height(self):
        if self.root != None:
            self._height(self.root, 0)
        else:
            return 0

    def _height(self, current_node, current_height):
        if current_node == None:
            return current_height

        left_height = self._height(current_node.left_child, current_height+1)
        right_height = self._height(current_node.right_child, current_height+1)

        return max(left_height, right_height)


    # search functionality

    def search(self, value):
        if self.root != None:
            self._search(value, self.root)
        else:
            return None

    def _search(self, value, current_node):
        if value == current_node.value:
            return True
        elif value < current_node.value and current_node.left_child != None:
            return self._search(value, current_node.left_child)
        elif value > current_node.value and current_node.right_child != None:
            return self._search(value, current_node.right_child)
        else:
            return False


    # inorder traversal of a tree

    def inorder(self):
        if self.root != None:
            self._inorder(self.root)

    def _inorder(self, current_node):
        if current_node != None:
            self._inorder(current_node.left_child)
            print(str(current_node.value))
            self._inorder(current_node.right_child)

    # preorder traversal of a tree

    def preorder(self):
        if self.root != None:
            self._preorder(self.root)

    def _preorder(self, current_node):
        if current_node != None:
            print(str(current_node.value))
            self._preorder(current_node.left_child)
            self._preorder(current_node.right_child)

    # postorder traversal of a tree

    def postorder(self):
        if self.root != None:
            self._postorder(self.root)

    def _postorder(self, current_node):
        if current_node != None:
            self._postorder(current_node.left_child)
            self._postorder(current_node.right_child)
            print(str(current_node.value))


tree = BST()
tree.insert(5)
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(7)
tree.insert(6)
tree.insert(8)
# tree.insert(3)
# tree.insert(6)
#tree.insert(4)
print("inorder")
tree.inorder()
print("preorder")
tree.preorder()
print("postorder")
tree.postorder()
print("tree height is " +str(tree.height()))