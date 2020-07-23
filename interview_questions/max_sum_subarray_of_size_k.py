'''
Given an array of integers and a number k, find maximum sum of a subarray of size k
Input  : arr[] = {1, 4, 2, 10, 23, 3, 1, 0, 20}
         k = 4
Output : 39
We get maximum sum by adding subarray {4, 2, 10, 23}
of size 4.
'''

def maxSum(arr, n, k):
    if n<k:
        print("invalid")
        return -1

    # Compute sum of first
    # window of size k
    res = 0
    for i in range(k):
        res += arr[i]
    # print(res)

    # Compute sums of remaining windows by
    # removing first element of previous
    # window and adding last element of
    # current window.

    curr_sum = res
    for i in range(k, n):
        curr_sum += arr[i] - arr[i-k]
        res = max(res, curr_sum)

    return res

arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 4
n = len(arr)
print(maxSum(arr, n, k))
