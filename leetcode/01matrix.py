'''
Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.
Example 1:

Input:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Output:
[[0,0,0],
 [0,1,0],
 [0,0,0]]
Example 2:

Input:
[[0,0,0],
 [0,1,0],
 [1,1,1]]

Output:
[[0,0,0],
 [0,1,0],
 [1,2,1]]


Solution:
1. Do a BFS search and mark 0 element as visited.
2. For each non zero element that is not visited check its left, right, top and bottom elements and increase the non visited element value by 1 and mark it as visited

'''

def oimatrix_leetcode(matrix):
    if matrix is None or len(matrix) == 0:
        return matrix

    m = len(matrix) # length of a row
    n = len(matrix[0]) # length of column

    queue = []
    visited = [[0 for i in range(n)] for j in range(m)]

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                queue.append([i, j])
                visited[i][j] = True

    print(queue)

    directions = [[0,1], [0,-1], [1,0], [-1,0]]

    while len(queue) > 0:
        curr = queue.pop(0)

        curr_x = curr[0]
        curr_y = curr[1]

        for direction in directions:
            x = curr_x + direction[0]
            y = curr_y + direction[1]

            if x<0 or x>m-1 or y<0 or y>n-1 or visited[x][y]:
                continue

            matrix[x][y] = matrix[curr_x][curr_y] + 1
            queue.append([x,y])
            visited[x][y] = True

    return matrix


a = [[0,0,0],[0,1,0],[1,1,1]]
print(oimatrix_leetcode(a))

