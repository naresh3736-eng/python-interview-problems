def count_spaces(string):
    words = string.split(" ")
    print(words)
    count = 1
    resutl_str = "" +words[0]
    print(resutl_str)

    for i in range(1, len(words)-1):
        if words[i] == "":
            count += 1
        else:
            resutl_str += str(count)
            count = 1
            resutl_str += words[i]
    if count != 0:
        resutl_str += str(count)
    return resutl_str

string = "hello world how  are  you "
print(count_spaces(string))