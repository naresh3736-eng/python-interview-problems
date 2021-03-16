def get_bits(string, index):
    if index < 0 or index > len(string):
        return 0
    if string[index] == 0:
        return 0
    else:
        return 1


def binary_addition(str1, str2):
    la = len(str1)
    lb = len(str2)

    maximum = max(la, lb)

    carry = 0
    result = []

    for i in range(maximum):
        m = get_bits(str1, la-i-1)
        n = get_bits(str2, lb-i-1)
        sum = m + n + carry
        result.append(sum % 2)
        carry = sum / 2

    if carry == 1:
        result.append(carry)

    return result[::-1]

print(binary_addition('11', '11'))


