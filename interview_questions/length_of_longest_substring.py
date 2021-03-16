'''
  The input string is ABDEFGABEF
  The length of the longest non-repeating character substring is 6
'''

# Brute Froce: O(n^3)

def lengthOfLongestSubstring(string):
    n = len(string)
    longest = 0

    for i in range(n):
        seen = set()

        for j in range(i, n):
            if string[j] in seen:
                break
            seen.add(string[j])
        longest = max(len(seen), longest)
    return longest


#print lengthOfLongestSubstring("ABDEFGABEF")


# Optmized approach: O(n)

def lengthOfLongestSubstring(string):
    left_most_valid = 0
    longest = 0
    last_seen = {}

    for i, letter in enumerate(string):
        if letter in last_seen:
            left_most_valid = max(left_most_valid, last_seen[letter] + 1)
        last_seen[letter] = i

        longest = max(longest, i-left_most_valid+1)

    return longest

print(lengthOfLongestSubstring("ABDEFGABEF"))