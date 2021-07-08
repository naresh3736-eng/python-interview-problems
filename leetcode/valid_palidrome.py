def validPalindrom(string):
    if not string:
        return
    if len(string) == 1:
        return True
    n = len(string)
    lp = 0
    rp = n-1

    while lp < rp:
        if string[lp] != string[rp]:
            return False
        else:
            lp += 1
            rp -= 1
    return True

print(validPalindrom("aba"))
