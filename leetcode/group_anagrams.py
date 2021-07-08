def groupAnagrams(strs: list):
    if not strs:
        return []
    lookup = {}
    for word in strs:
        sorted_word = ''.join(sorted(word))
        if sorted_word not in lookup:
            lookup[sorted_word] = [word]
        else:
            lookup[sorted_word].append(word)
    result = []
    for item in lookup.values():
        result.append(item)
    return result

print(groupAnagrams(["ate", 'tea', 'bat', 'tan', 'eat', 'nat']))