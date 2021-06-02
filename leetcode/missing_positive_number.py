def findMissingPostivieNumber(nums):
    nums = sorted(nums)
    temp = 1
    for i in nums:
        if i == temp:
            temp += 1
    return temp

myList = [ 2, 3, -7, 6, 8, -10, 15,1]
# print(findMissingPostivieNumber(myList))


def findMissingNumbers(list):
    ref_list = [*range(list[0], list[-1]+1, 1)]
    res = []
    i, j = 0, 0
    while i < len(ref_list) and j < len(list):
        if ref_list[i] == list[j]:
            i += 1
            j += 1
        elif ref_list[1] < list[j]:
            res.append(ref_list[i])
            i += 1
    return res


# print(findMissingNumbers([1,3,4,5,7,8,10]))

def findMissingPositiveNumberArithmeticWay(arr):
    arr_sum = 0
    n = len(arr) + 1
    # first find the sum of n numbers n(n+1)/2 for a given arr len + 1
    sum_of_n = n*(n+1)//2
    for i in arr:
        arr_sum += i
    missing_element = sum_of_n - arr_sum
    return missing_element

print(findMissingPositiveNumberArithmeticWay([1,2,3,5,6,7]))
