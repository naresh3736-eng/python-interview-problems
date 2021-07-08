'''
Given an integer array, count element x such that x+1 is also in arr
If there are duplicates in arr count them separetely
Example1:
input: arr = [1,2,3]
output: 2
explanation: 1 and 2 are counted cause 2 and 3 are in arr

Example2:
input: arr = [1,1,3,3,5,5,7,7]
output: 0
explanation: No numbers are counted because there are no 2, 4, 6, 8 in input arr
'''

def countElements(nums: list):
    if not nums:
        return 0
    lookup = {}
    result = 0
    for num in nums:
        lookup[num] = 1

    for num in nums:
        if num+1 in lookup:
            result += 1
    return result

print(countElements([1,2,3]))