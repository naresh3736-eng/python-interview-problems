"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.



Example 1:

Input: n = 19
Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 02 = 1
Example 2:

Input: n = 2
Output: false

SOLUTION:
Split the given number to calculate the sum of squares using the mathametical method num%10 and num//10
    example: 19 -> 19%10 = 9 -> 19//10 = 1 -> 9*9 + 1*1 = 82
Add the result of above to a set and repeat until we see a number 1 in the result and return True if 1 exists otherwise return False
"""

def sqsum(num):
    result = 0
    while num > 0:
        r = num % 10
        result = result + r * r
        num = num //10
    return result

def happyNumber(num):
    seen = set()
    while sqsum(num) not in seen:
        sum1 = sqsum(num)
        if sum1 == 1:
            return True
        else:
            seen.add(sum1)
            num = sum1
    return False

print(happyNumber(19))