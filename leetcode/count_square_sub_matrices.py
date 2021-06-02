"""
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.



Example 1:

Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation:
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.
Example 2:

Input: matrix =
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation:
There are 6 squares of side 1.
There is 1 square of side 2.
Total number of squares = 6 + 1 = 7.
"""

def countSuareSubMatrices(matrix):
    r, c = len(matrix), len(matrix[0])
    res = [[0]*(c+1) for i in range(r+1)]
    count = 0
    for i in range(1, r+1):
        for j in range(1, c+1):
            if matrix[i-1][j-1] == 1:
                res[i][j] = 1 + min(res[i][j-1], res[i-1][j], res[i-1][j-1])
                count += res[i][j]
    return count

print(countSuareSubMatrices([
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]))


