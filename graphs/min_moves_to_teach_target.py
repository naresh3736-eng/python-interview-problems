'''
Given a target position on infinite number line, i.e -infinity to +infinity. Starting form 0 you have to reach the target by moving as described : In ith move you can take i steps forward or backward. Find the minimum number of moves require to reach the target.
'''

'''
Examples:
Input : target = 3
Output : 2
Explanation:
On the first move we step from 0 to 1.
On the second step we step from 1 to 3.

Input: target = 2
Output: 3
Explanation:
On the first move we step from 0 to 1.
On the second move we step  from 1 to -1.
On the third move we step from -1 to 2.
'''

# recursive approach
import sys

def minMoves_rec(start, step, dest):
    if abs(start) > dest:
        return sys.maxsize

    if start == dest:
        return step

    pos = minMoves_rec(start + step + 1, step + 1, dest)

    neg = minMoves_rec(start - step - 1, step + 1, dest)

    return min(pos, neg)


# print minMoves_rec(0,0,11)


# optimized solution

def minMoves_efficient(target):
    target = abs(target)

    sum = 0
    step = 0

    while sum < target or (sum - target) % 2 !=0:
        step += 1
        sum += step

    return step

print(minMoves_efficient(2))
