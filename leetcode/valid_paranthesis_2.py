'''
Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
'''

def validParanthesis(string):
    if len(string) == 0 or string == "*":
        return True
    if len(string) == 1:
        return False

    leftcounter = 0
    rightcounter =0

    for char in string:
        if char == ')':
            leftcounter -= 1
        else:
            leftcounter += 1

        if leftcounter < 0:
            return False
    if leftcounter == 0:
        return True

    for char in reversed(string):
        if char == '(':
            rightcounter -= 1
        else:
            rightcounter += 1

        if rightcounter < 0:
            return False
    return True

print(validParanthesis("((*))"))