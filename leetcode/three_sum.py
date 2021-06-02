'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
Solution: 1. First sort the given array in ascending order
          2. Iterate through the array and
                a. for each element in array set the lp to next index and rp to last index
                b. calculate the sum of current element + element at lp + element at rp
                c. if sum = 0 then increment lp and decrement rp by 1
                    elif sum < 0 then increment lp by 1
                    else sum > 0 then decrment rp by 1
'''


def threeSum(arr):
    arr.sort()
    res = []
    n = len(arr)
    for i in range(n-2): # itereting till n-2 to have buffer for left and right pointers
        if i > 0 and arr[i] == arr[i-1]: # to avoid duplicates of first element that is i
            continue
        lp = i+1
        rp = n-1
        while lp < rp:
            sum = arr[i] + arr[lp] + arr[rp]
            if sum < 0:
                lp += 1
            elif sum > 0:
                rp -= 1
            else:
                res.append([arr[i], arr[lp], arr[rp]])
                # to avoid duplicates at lp and rp
                while lp < rp and arr[lp] == arr[lp+1]:
                    lp += 1
                while lp < rp and arr[rp] == arr[rp-1]:
                    rp -= 1
                lp += 1
                rp -= 1
    return res

arr = [-1,0,1,2,-1,-4]
print(threeSum(arr))