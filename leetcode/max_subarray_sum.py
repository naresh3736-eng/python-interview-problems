"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.



Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23


Constraints:

1 <= nums.length <= 3 * 104
-105 <= nums[i] <= 105
"""

def maxSubarray(nums):
    total_sum = max_sum = nums[0]
    for i in nums[1:]:
        total_sum = max(total_sum+i, i)
        max_sum = max(max_sum, total_sum)
    return max_sum

print(maxSubarray([-5,3,-5]))