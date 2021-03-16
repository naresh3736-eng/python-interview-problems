'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        longest = 0
        left_most_valid = 0
        last_seen = {}

        for i, let in enumerate(s):
            if let in last_seen:
                left_most_valid = max(left_most_valid, last_seen[let] + 1)
            last_seen[let] = i
            longest = max(longest, i - left_most_valid + 1)
            print(longest)

        return longest

if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLongestSubstring("abcab"))