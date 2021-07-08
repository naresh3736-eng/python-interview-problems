'''
In an alien dictionary, surprisingly they also use endlish lowercas letters, but possibly in a different order.
The order of the alphabet is some purmutation of lowercase letters
Given a sequence of words written in the alien language, and the order of the aplhabet, return true if only if the give
words are sorted lexicographically in this alien language.

Example1:
Input words: ["hello", "leetcode"], order="hlabcdefgijkmnopqrstuvwxyz"
Outpt: True
Explanation: As 'h' comes befor 'h' in this language, then the sequence is sorted

Example2:
Input words: ["word, "world", "row"], order = worldabcefghijkmnpqstuvxyz"
Output: False
Explanaiton: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted

Example3:
Input words: ["apple", "app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: False
Explanation: The first three characters "app" match and the second string shorter in size. According to lexicographical
rules "apple" > "app" because "l" > "0", where 0 is defined as blank character
'''

def alienDictionary(words: list, order: str):
    lookup = {v:i for i, v in enumerate(order)}
    for i in range(len(words)-1):
        word1 = words[i]
        word2 = words[i+1]
        if len(word1) > len(word2):
            return False
        for j in range(len(word1)):
            # if j == len(word2):
            #     return False
            if lookup[word1[j]] < lookup[word2[j]]:
                break
            if lookup[word1[j]] > lookup[word2[j]]:
                return False
    return True

print(alienDictionary(["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))
print(alienDictionary(["word", "world", "row"], "worldabcefghijkmnpqstuvxyz"))
print(alienDictionary(["apple", "app"], "abcdefghijklmnopqrstuvwxyz"))