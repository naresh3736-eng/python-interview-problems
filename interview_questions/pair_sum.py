'''
return the pairs that adds up to a given target
input: ([1,3,2,2], 4)
output: (1,3) (2,2)
'''

def pairSum(arr, target):
    if len(arr) <= 0:
        return 0

    seen = set()
    output = []

    for num in arr:
        compliment = target - num

        if compliment not in seen:
            seen.add(num)
        else:
            output.append([min(num, compliment), max(num, compliment)])

    print '\n'.join(map(str, list(output)))



#pairSum([1,3,3,1], 4)


def pari_sum(arr, target):
    if len(arr) < 1:
        return 0

    lookup = {}
    output = []

    for i, num in enumerate(arr):
        compliment = target - num
        if compliment in lookup:
            if abs(lookup[compliment] - i) == 1:
                output.append((compliment, num))
        lookup[num] = i
        print lookup
        print output

    return output

print pari_sum([1,3,3,1], 4)