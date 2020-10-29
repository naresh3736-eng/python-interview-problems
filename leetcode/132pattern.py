"""
Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].

Return true if there is a 132 pattern in nums, otherwise, return false.

Follow up: The O(n^2) is trivial, could you come up with the O(n logn) or the O(n) solution?



Example 1:

Input: nums = [1,2,3,4]
Output: false
Explanation: There is no 132 pattern in the sequence.
Example 2:

Input: nums = [3,1,4,2]
Output: true
Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
Example 3:

Input: nums = [-1,3,2,0]
Output: true
Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
"""

# solution 1 (Brute Force) O(n^3)

def find132pattern1(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if nums[i] < nums[k] < nums[j]:
                    return True
    return False


print(find132pattern1([3,1,4,2]))

# solution 2 (improvised) O(n^2)

def find132pattern2(nums):
    leftmin = nums[0]

    for j in range(1, len(nums)):
        for k in range(j+1, len(nums)):
            if nums[k] > leftmin and nums[j] > nums[k]:
                return True
        leftmin = min(leftmin, nums[j])
    return False

print(find132pattern2([1,2,3,4]))

# solution 3 (optimized) O(n)
def find132pattern3(nums):
    min_array = [0] * len(nums)
    min_array[0] = nums[0]

    for i in range(1, len(nums)):
        min_array[i] = min(min_array[i-1], nums[i])
    # print(min_array)

    stack = []
    for j in range(len(nums)-1, -1, -1):
        if nums[j] > min_array[j]: # checking nums[i] < nums[j]
            while stack and stack[-1] <= min_array[j]: # popping the stack if any nums[k] exists that is <= nums[i]
                stack.pop(-1)
            if stack and stack[-1] < nums[j]: # checking nums[k] < nums[j]
                return True

            stack.append(nums[j])

    return False

print(find132pattern3([1,2,3,4]))