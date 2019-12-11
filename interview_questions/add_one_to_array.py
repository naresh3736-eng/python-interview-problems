'''
for a given array of elements add one and return the immediate next highest number
ex1: [1,3,4,5] --> [1,3,4,6]
ex2: [1,9,9] --> [2,0,0]
ex3: [9,9,9] --> [1,0,0,0]
'''

def add_one_to_array(arr):
    if len(arr) <= 0:
        return 0
    carry = 1
    result = [0] * (len(arr))
    for i in xrange(len(arr)-1, -1, -1):
        sum = arr[i] + carry

        if sum == 10:
            carry = 1
        else:
            carry = 0
            result[i] = sum % 10
    if carry == 1:
        result = [0] * (len(arr) + 1)
        result[0] = carry

    return result

print add_one_to_array([1,9,9])