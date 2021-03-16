def validParanthesis(string):
    lookup = {"{": "}", "[": "]", "(": ")"}

    stack = []

    for char in string:
        if char in lookup:
            stack.append(char)
        elif len(stack) == 0 or lookup[stack.pop()] != char:
            return False

    return len(stack) == 0

print(validParanthesis("{([()])}"))