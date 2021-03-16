'''
Given a adjacency matrix, traverse the graph
'''

def bfs_traversal(matrix):
    if len(matrix) <=0:
        return

    queue = [0]
    visited = [0] * int(len(matrix))
    visited[0] = 1

    while len(queue) >= 1:
        node = queue[0]
        queue.pop(0)
        print(node)

        for i in range(0, len(visited)):
            if matrix[node][i] == 1 and visited[i] == 0:
                visited[i] = 1

                queue.append(i)

matrix = [[1,0,0,0,1],
          [0,1,1,0,0]]

bfs_traversal(matrix)