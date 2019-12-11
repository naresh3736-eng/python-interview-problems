'''
Given an unsorted list of integers find the length of longest consecutive sub list
Input: [2,4,3,6,1,8]
output: 4 [1,2,3,4]
'''


def longest_consecutive_seq(arr):
    numDict = {}

    max_l = 1

    for i in range(len(arr)):
        numDict[arr[i]] = 1

    for i in range(len(arr)):
        if arr[i] in numDict:
            k = 1
            count = 1

            while arr[i]-k in numDict:
                count += 1
                del numDict[arr[i]-k]
                k += 1

            k = 1

            while arr[i]+k in numDict:
                count += 1
                del numDict[arr[i]+k]
                k += 1
            max_l = max(max_l, count)

    return max_l


arr = [2,4,3,6,1,8,9,10,11,12]

arr1 = [2,4,3,6,1,8]

print longest_consecutive_seq(arr1)
