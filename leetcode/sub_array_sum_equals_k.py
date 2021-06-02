def subArraySum(arr, k):
    cum_sum = 0
    lookup = {0:1}
    count = 0

    for num in arr:
        cum_sum += num
        if cum_sum - k in lookup:
            count += lookup[cum_sum - k]
        if cum_sum in lookup:
            lookup[cum_sum] += 1
        else:
            lookup[cum_sum] = 1
    return count

arr = [3,4,7,2,-3,1,4,2]
k = 7
print(subArraySum(arr, k))