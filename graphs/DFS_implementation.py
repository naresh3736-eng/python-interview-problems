'''
Givne a adjacency matrix, traverse the graph using DFS algorithm
'''


def dfs_traversal(matrix):
    if len(matrix) <= 1:
        return

    stack = [0]  # start from node 0
    visited = [0] * int(len(matrix))

    visited[0] = 1  # set the ndoe 0 as visited

    while len(stack) >= 1:
        node = stack.pop()
        print(node)

        for i in range(0, len(visited)):
            if matrix[node][i] == 1 and visited[i] == 0:  # check if the route exista and it is visited
                visited[i] = 1
                stack.append(i)


matrix = [[0, 1, 0, 1],
          [1, 0, 0, 0]]

dfs_traversal(matrix)
