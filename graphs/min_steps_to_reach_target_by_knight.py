'''
Given a square chessboard of N x N size, the position of Knight and position of a target is given. We need to find out minimum steps a Knight will take to reach the target position.
'''

class cell:
    def __init__(self, x=0, y=0, dist=0):
        self.x = x
        self.y = y
        self.dist = dist


def isInside(x, y, N):
    if (x>=1 and x<=N and y>=1 and y<=N):
        return True
    return False


def minStepsToReachTarget(knightPos, targetPos, N):

    #all possible movements for the knight

    dx = [2,2,-2,-2,1,1,-1,-1]
    dy = [1,-1,1,-1,2,-2,2,-2]

    queue = []

    # push starting position of the knight with dist 0 into queue

    queue.append(cell(knightPos[0], knightPos[1], 0))

    # mark all cells unvisited

    visited = [[False for i in range(N+1)] for j in range(N+1)]

    # visit the starting state

    visited[knightPos[0]][knightPos[1]] = True

    while len(queue) > 0:
        t = queue[0]
        queue.pop(0)

        if t.x == targetPos[0] and t.y == targetPos[1]:
            return t.dist

        for i in range(8):
            x = t.x + dx[i]
            y = t.y + dy[i]

            if isInside(x, y, N) and not visited[x][y]:
                visited[x][y] = True
                queue.append(cell(x, y, t.dist + 1))

if __name__=='__main__':
    N = 30
    knightpos = [1, 1]
    targetpos = [30, 30]
    print minStepsToReachTarget(knightpos, targetpos, N)