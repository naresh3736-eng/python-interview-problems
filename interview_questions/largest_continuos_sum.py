def largest_cont_sum(arr):
    if len(arr) == 0:
        return 0
    max_sum = curr_sum = arr[0]

    for num in arr[1:]:
        curr_sum = max(curr_sum+num , num)
        max_sum = max(max_sum, curr_sum)

    return max_sum

# print largest_cont_sum([1,2,3,4,-1,10,10,-10,-1])

# print largest_cont_sum([-2, -3, 4, -1, -2, 1, 5, -3])

from sys import maxsize


# Function to find the maximum contiguous subarray
# and print its starting and end index
def maxSubArraySum(a, size):
    max_so_far = -maxsize - 1
    max_ending_here = 0
    start = 0
    end = 0
    s = 0

    for i in range(0, size):

        max_ending_here += a[i]

        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            start = s
            end = i

        if max_ending_here < 0:
            max_ending_here = 0
            s = i + 1

    return (end - start + 1)


# Driver program to test maxSubArraySum
a = [-2, -3, 4, -1, -2, 1, 5, -3]
print(maxSubArraySum(a, len(a)))