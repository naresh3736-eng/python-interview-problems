'''
Given two strings s1 and s2, return true if s2 contains the permutation of s1.

In other words, one of s1's permutations is the substring of s2.

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
'''

from collections import Counter, defaultdict
def permutationsInString(s1: str, s2: str):
    if len(s1) > len(s2):
        return False

    len_of_s1 = len(s1)
    # s1_counter = Counter(s1)
    # window_counter = Counter()

    '''
    using defaultdict which speeds up the execution time compared to using Counter
    '''
    s1_counter = defaultdict(int)
    window_counter = defaultdict(int)
    for c in s1:
        s1_counter[c] += 1

    for i, c in enumerate(s2):
        window_counter[c] += 1
        if i >= len_of_s1:
            element_from_left = s2[i-len_of_s1]
            if window_counter[element_from_left] == 1:
                del window_counter[element_from_left]
            else:
                window_counter[element_from_left] -= 1

            if s1_counter == window_counter:
                return True
    return False

print(permutationsInString('ab', 'eidbaooo'))