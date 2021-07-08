'''
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''
def threeSumClosest(nums: list, target: int):
    nums.sort()
    res = sum(nums[:3])

    for i in range(len(nums)-2):
        lp = i + 1
        rp = len(nums)-1

        while lp < rp:
            sumhere = nums[i] + nums[lp] + nums[rp]
            if abs(sumhere-target) < abs(res-target):
                res = sumhere
            if sumhere < target:
                lp += 1
            else:
                rp -= 1
    return res

print(threeSumClosest([-1,2,1,-4], 1))
