"""
We have two special characters. The first character can be represented by one bit 0. The second character can be represented by two bits (10 or 11).

Now given a string represented by several bits. Return whether the last character must be a one-bit character or not. The given string will always end with a zero.

Example 1:
Input:
bits = [1, 0, 0]
Output: True
Explanation:
The only way to decode it is two-bit character and one-bit character. So the last character is one-bit character.
Example 2:
Input:
bits = [1, 1, 1, 0]
Output: False
Explanation:
The only way to decode it is two-bit character and two-bit character. So the last character is NOT one-bit character.

Solution: Loop through the given bits and when 1 is encountered skip the next element and increment the loop counter by 1. Once the end of the list is reached
check wheter the loop counter equals the size of the bits array and return flag
"""

def isOneBitCharacter1(bits):
    flag = False
    i = 0
    while i < (len(bits)):
        if(i == len(bits) -1 ):
            flag = True

        if (bits[i] == 1):
            i += 1
        i += 1
    return flag

bits = [1,1,1,0]
print(isOneBitCharacter1(bits))

# OR

def isOneBitCharacter2(bits):
    flag = False
    i = 0
    while i < len(bits):
        if bits[i] == 0:
            flag = True
            i += 1
        elif bits[i] == 1:
            flag = False
            i += 2
    return flag

bits = [1,0,0]
print(isOneBitCharacter2(bits))