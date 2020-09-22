def stringCompression(string):
    result = ""
    count = 1

    result += string[0]

    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            count += 1
        else:
            # if count >= 1:
            #     result += str(count)
            result += str(count)
            result += string[i+1]
            count = 1

    if count >= 1:
        result += str(count)

    return result


print stringCompression("abbccdd")