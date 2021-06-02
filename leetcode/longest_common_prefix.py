"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.

SOLUTION:
First find the min length string from a given list because the common prefix is going to be less than or equal to the min len string
Loop through until the min length from above step and compare the strings to find the prefix
"""

def longestCommonPrefix(strs):
    if len(strs) == 0:
        return ""
    minlen = len(strs[0])
    for string in strs:
        minlen = min(minlen, len(string))

    lcp = ""
    i = 0
    while i < minlen:
        char = strs[0][i]
        for j in range(1, len(strs)):
            if strs[j][i] != char:
                return lcp
        lcp = lcp + char
        i += 1
    return lcp

print(longestCommonPrefix(["flower","flow","flight"]))
print(longestCommonPrefix(["dog","racecar","car"]))