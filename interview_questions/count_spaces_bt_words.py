def count_spaces(string):
    words = string.split(" ")
    count = 1
    resutl_str = "" +words[0]

    for i in range(1, len(words)):
        if words[i] == "":
            count += 1
        else:
            resutl_str += str(count)
            count += 1
            resutl_str += words[i]
    return resutl_str


