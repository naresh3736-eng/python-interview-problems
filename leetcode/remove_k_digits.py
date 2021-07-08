'''
Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
'''

def removeKDigits(nums: list, k: int):
    stack = []
    nums_to_remove = k
    for curr_element in nums:
        while nums_to_remove and stack and stack[-1] > curr_element:
            stack.pop()
            nums_to_remove -= 1
        stack.append(curr_element)
    ans = ''.join(stack[0:len(nums)-k]).lstrip('0')

    if ans:
        return ans
    else:
        return "0"

print(removeKDigits("1432219", 3))