'''
Given a number N which is the total number of nodes in a complete binary tree where nodes are number from 1 to N sequentially level-wise.
The task is to write a program to print paths from root to all of the nodes in the Complete Binary Tree.
'''

# Function to print path of all the nodes
# nth node represent as given node kth
# node represents as left and right node

def printPath(res, nthNode, kthNode):
    # base condition
    # if kth node value is greater
    # then nth node then its means
    # kth node is not valid so
    # we not store it into the res
    # simply we just return

    if kthNode > nthNode:
        return

    # Storing node into res
    res.append(kthNode)

    # Print the path from root to node
    for i in range(0, len(res)):
        #print(res[i], end=' ')
        pass
    print()

    # store left path of a tree
    # So for left we will go node(kThNode*2)
    printPath(res, nthNode, kthNode * 2)

    # right path of a tree
    # and for right we will go node(kThNode*2+1)
    printPath(res, nthNode, kthNode * 2 + 1)


# Function to print path from root
# to all of the nodes
def printPath_to_cover_all_nodes(nthNode):
    res = []

    printPath(res, nthNode, 1)

# Driver Code
if __name__ == "__main__":
    # Given Node
    nThNode = 7

    # Print path from root to all node.
    printPath_to_cover_all_nodes(nThNode)