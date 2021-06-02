"""
Given a circular array circ of integers represented by nums, find the maximum possible sum of a non-empty subarray of circ.

Here, a circular array means the end of the array connects to the beginning of the array.  (Formally, circ[i] = nums[i] when 0 <= i < nums.length, and circ[i+nums.length] = circ[i] when i >= 0.)

Also, a subarray may only include each element of the fixed buffer nums at most once.  (Formally, for a subarray circ[i], circ[i+1], ..., circ[j], there does not exist i <= k1, k2 <= j with k1 % nums.length = k2 % nums.length.)



Example 1:

Input: nums = [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3
Example 2:

Input: nums = [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10
Example 3:

Input: nums = [3,-1,2,-1]
Output: 4
Explanation: Subarray [2,-1,3] has maximum sum 2 + (-1) + 3 = 4
Example 4:

Input: nums = [3,-2,2,-3]
Output: 3
Explanation: Subarray [3] and [3,-2,2] both have maximum sum 3
Example 5:

Input: nums = [-2,-3,-1]
Output: -1
Explanation: Subarray [-1] has maximum sum -1

SOLUTION:
Take max sum subarray of a given array
calculate the sum of array elements (total sum)
multiply array elements by -1
take the max sum subarray of new multiplied array
add new max sum subarray value to total sum
if new total sum is greater than max sum subarray of original array and it is not equal to 0 then return new total sum else return max sum subarray of original array
"""

def maxSumSubArray(nums: list):
    max_sum = total_sum = nums[0]
    for i in nums[1:]:
        total_sum = max(total_sum+i, i)
        max_sum = max(max_sum, total_sum)
    return max_sum

def maxSumCircularSubArray(nums):
    k = maxSumSubArray(nums)
    cs = 0
    for i in range(len(nums)):
        cs += nums[i]
        nums[i] = -nums[i]
    cs = cs + maxSumSubArray(nums)

    if cs > k and cs != 0:
        return cs
    else:
        return k

print(maxSumCircularSubArray([1,-2,3,-2]))