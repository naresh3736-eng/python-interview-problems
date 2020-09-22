'''
Given an array of integers, return indices of the two numbers such that they add up to a specific targer.
Yoy may assume that each input would have exactly one solution, and you may not use the same element twice
Example:
    nums = [2,7,11,15], target = 9
    return [0, 1]
'''

def twoSum(nums, target):
    lookup = {}
    for i, num in enumerate(nums):
        compliment = target - num
        if compliment in lookup:
            return [lookup[compliment], i]
        lookup[num] = i


nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))