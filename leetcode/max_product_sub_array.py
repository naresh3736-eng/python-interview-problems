def maxProductSubArray(nums):
    max_product = max_value = min_value = nums[0]

    for num in nums[1:]:
        # when a negative number the max_value becomes min_value and min_value becomes max_value
        if num < 0:
            min_value, max_value = max_value, min_value

        max_value = max(max_value * num, num)
        min_value = min(min_value * num, num)

        max_product = max(max_value, max_product)
    return max_product

print(maxProductSubArray([2,3,-2,4]))
