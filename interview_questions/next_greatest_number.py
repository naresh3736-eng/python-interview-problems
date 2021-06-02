'''
input - 38627
output - 38672
'''

def nextgreatest(arr):
    i = max(i for i in range(1, len(arr)) if arr[i-1] < arr[i])
    j = max(j for j in range(i, len(arr)) if arr[i-1] < arr[j])

    arr[j], arr[i-1] = arr[i-1], arr[j]

    arr[i:] = reversed(arr[i:])

    print(int(''.join(arr)))


n = 38276
n = 59853
array = list(str(n))
nextgreatest(array)