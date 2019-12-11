def stringMultiplication(s1, s2):
    s1 = s1[::-1]
    s2 = s2[::-1]
    output = []
    result = int(len(s1) + len(s2)) * [0]

    for i in range(len(s1)):
        for j in range(len(s2)):
            result[i+j] += int(s1[i]) * int(s2[j])
    print result

    for k in range(0, len(result)-1):
        mod = result[k]%10
        carry = result[k]/10

        if k+1 < len(result):
            result[k+1] += carry
        output.insert(0, mod)

    return output

print stringMultiplication("25", "25")
