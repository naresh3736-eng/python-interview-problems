"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.



Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.


Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104

SOLUTION:
First sort the given intervals array on first element of sub-array
To find overlap do the follwing:
    If first element of i+1 th sub-array is less than or equal to second element of i th sub-array then
        Update ith sub-array as first-element = min(i[0], i+1[0]), second-element = max(i[1], i+1[1])
        Delete the i+1 th element/sub-array
"""

def mergeIntervals(intervals: list):
    if len(intervals) <= 0:
        return
    # sort the intervals array on the first element of each sub-array
    intervals.sort(key=lambda x: x[0])
    i = 1
    while i < len(intervals):
        if intervals[i][0] <= intervals[i-1][1]:
            intervals[i-1][0] = min(intervals[i-1][0], intervals[i][0])
            intervals[i-1][1] = max(intervals[i-1][1], intervals[i][1])

            intervals.pop(i)
        else:
            i += 1
    return intervals

print(mergeIntervals([[1,3],[2,6],[8,10],[15,18]]))
