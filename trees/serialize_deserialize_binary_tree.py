'''
erialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.
Example1:
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]

Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
Example 4:

Input: root = [1,2]
Output: [1,2]
'''

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

class Codec:
    def serialize(self, root: TreeNode):
        return self.helper_serialize(root, '')

    def helper_serialize(self, root: TreeNode, string):
        if root is None:
            string += 'None'
        else:
            string += str(root.val) + ','
            string = self.helper_serialize(root.left, string)
            string = self.helper_serialize(root.right, string)
        return string

    def deserialize(self, data: str):
        data_list = data.split(',')
        root = self.helper_deserialize(data_list)
        return root

    def helper_deserialize(self, slist: list):
        if slist[0] == 'None,':
            slist.pop(0)
            return None
        else:
            root = TreeNode(slist[0])
            slist.pop(0)
            root.left = self.helper_deserialize(slist)
            root.right = self.helper_deserialize(slist)
        return root