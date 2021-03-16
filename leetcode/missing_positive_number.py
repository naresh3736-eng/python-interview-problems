def findMissingPostivieNumber(nums):
    nums = sorted(nums)
    temp = 1
    for i in nums:
        if i == temp:
            temp += 1
    return temp

myList = [ 2, 3, -7, 6, 8, -10, 15,1]
print(findMissingPostivieNumber(myList))
