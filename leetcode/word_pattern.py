'''
Given a pattern and a string find if string follows the pattern
Example1:
Input: pattern = "abba", string = "dog cat cat dog"
Output: True

Example2:
Input: pattern = "abba", string = "dog cat cat fish"
Output: False

Example3:
Input: pattern = "aaaa", string = "dog cat cat dog"
Output: False
'''

def wordPattern(pattern: str, string: str) -> bool:
    words = string.split(" ")
    if len(pattern) != len(words):
        return False
    char_to_words = {}
    for char, word in zip(pattern, words):
        if char in char_to_words and char_to_words[char] != word:
            return False
        else:
            char_to_words[char] = word
    return True

print(wordPattern("abba", "dog cat cat dog"))