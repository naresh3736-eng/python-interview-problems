def permutation(string):
    output = []

    if len(string) == 1:
        return string
    else:
        for i, let in enumerate(string):

            for perm in permutation(string[:i] + string[i+1:]):
                output += [let + perm]

        return output

print permutation("abc")