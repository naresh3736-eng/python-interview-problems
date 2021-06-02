'''
solution: loop throug the given string and check for below:
            if prev < curr then prev + curr - 2*prev
            else prev + curr
            When ever we encounter a patter like IX or IV then the total should be 9 (1+10-2*1) or 4 (1+5-2*1)
'''
def romanToInteger(s):
    lookup = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    prev = 0
    curr = 0
    total = 0

    for i in range(len(s)):
        curr = lookup[s[i]]
        if curr > prev:
            total = total + curr - 2*prev
        else:
            total = total + curr
        prev = curr
    return total

print(romanToInteger("XLIX"))
