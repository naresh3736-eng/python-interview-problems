def get_bits(string, index):
    if index < 0 or index > len(string):
        return 0
    if string[index] == 0:
        return 0
    else:
        return 1

def binarySum(s1, s2):
    la = len(s1)
    lb = len(s2)

    maximum = max(la, lb)
    carry = 0
    result = []

    for i in range(maximum):
        m = get_bits(s1, la-i-1)
        n = get_bits(s2, lb-i-1)

        sum = m + n + carry

        result.append(sum % 2)
        carry = sum //2
    if carry == 1:
        result.append(carry)

    return result[::-1]


if __name__ == "__main__":
    s1 = "110"
    s2 = "110"

    print binarySum(s1, s2)

