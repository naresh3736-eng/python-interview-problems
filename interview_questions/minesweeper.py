def solution(N, R, C):
    res = [[0]*N for i in range(N)]
    directions = [(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]
    for i, j in zip(R, C):
        res[i][j] = 'B'

    for i in range(N):
        for j in range(N):
            if res[i][j] == 'B':
                continue
            count = 0
            for direction in directions:
                x = direction[0] + i
                y = direction[1] + j
                if x<0 or x>N-1 or y<0 or y>N-1:
                    continue
                if res[x][y] == 'B':
                    count += 1
            res[i][j] = count
    return res

print(solution(3, [2,1,0,2], [0,2,1,2]))