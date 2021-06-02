import random
def pickIndex(weights: list):
    prefix_sum_arr = []
    prefix_sum = 0
    for weight in weights:
        prefix_sum += weight
        prefix_sum_arr.append(prefix_sum)
    total_sum = prefix_sum

    randon_num = random.random() * total_sum
    low, high = 0, len(prefix_sum_arr)
    while low < high:
        mid = low + (high- low) //2
        if randon_num > prefix_sum_arr[mid]:
            low = mid + 1
        else:
            high = mid
    return low

print(pickIndex([1,3]))