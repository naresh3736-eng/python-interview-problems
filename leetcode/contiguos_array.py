'''
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.
Example 1:

Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
Example 2:

Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
'''

def contiguosArray(nums):
    subarray = count = 0
    lookup = {}
    for i in range(len(nums)):
        if nums[i] == 1:
            count += 1
        else:
            count -= 1
        if count == 0:
            subarray = i + 1
        if count in lookup:
            subarray = max(subarray, i-lookup[count])
        else:
            lookup[count] = i
    return subarray

print(contiguosArray([0,0,1,0,0,1,1]))