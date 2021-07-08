'''
Given a string s, return the first non-repeating character in it and return its index. If it does not exist, return -1.
Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1
'''

def firstUniqueCharacter(s: str):
    lookup = {}
    for char in s:
        if char in lookup:
            lookup[char] += 1
        else:
            lookup[char] = 1

    for i in range(len(s)):
        if lookup[s[i]] == 1:
            return i
    return -1

# from collections import defaultdict
# def sol2(s: str):
#     lookup = defaultdict(int)
#     for char in s:
#         if char in lookup:
#             lookup[char] += 1
#         else:
#             lookup[char] = 1
#
#     for i in range(len(s)):
#         if lookup[s[i]] == 1:
#             return i
#     return -1

print(firstUniqueCharacter("leetcode"))
print(firstUniqueCharacter("laoveleetcode"))
print(firstUniqueCharacter("aabb"))

# print(sol2("laoveleetcode"))