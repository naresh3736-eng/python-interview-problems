"""
Given an array of n distinct elements, find the minimum number of swaps required to sort the array.
Examples:

Input : {4, 3, 2, 1}
Output : 2
Explanation : Swap index 0 with 3 and 1 with 2 to
              form the sorted array {1, 2, 3, 4}.

Input : {1, 5, 4, 3, 2} {1,2,3,4,5}
Output : 2
"""

def minSwaps(arr):
    ref_arr = sorted(arr)
    lookup = {v:i for i, v in enumerate(arr)}
    swaps = 0

    for i, v in enumerate(arr):
        actual_pos_val = ref_arr[i]
        if v!=actual_pos_val:
            to_swap_idx = lookup[actual_pos_val]
            arr[i], arr[to_swap_idx] = arr[to_swap_idx], arr[i]
            lookup[v] = to_swap_idx
            lookup[actual_pos_val] = i
            swaps += 1
    print(swaps)
    print(arr)

arr = [4, 3, 2, 1, 8, 6, 0]
minSwaps(arr)
