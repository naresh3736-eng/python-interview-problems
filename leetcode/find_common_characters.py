'''
Given an array words of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

You may return the answer in any order.

Example 1:

Input: ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: ["cool","lock","cook"]
Output: ["c","o"]
'''

from collections import Counter, defaultdict

def commonCharacters(words):
    res = []
    cl = Counter(words[0])

    for word in words[1:]:
        temp = Counter(word)
        for key in list(cl.keys()):
            if key not in temp:
                del cl[key]
            else:
                cl[key] = min(cl[key], temp[key])
    for key in cl:
        res += [key] * cl[key]
    return res

print(commonCharacters(["bella","label","roller"]))

# using default dict
def commonCharacters1(words):
    res = []
    def get_dict(string):
        tmp = defaultdict(int)
        for char in string:
            if char in tmp:
                tmp[char] += 1
            else:
                tmp[char] = 1
        return tmp

    cl = get_dict(words[0])

    for word in words[1:]:
        temp = get_dict(word)
        for key in list(cl.keys()):
            if key not in temp:
                del cl[key]
            else:
                cl[key] = min(cl[key], temp[key])
    for key in cl:
        res += [key] * cl[key]
    return res

print(commonCharacters1(["bella","label","roller"]))