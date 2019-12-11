def pythogaranTriplet(arr):
    for i in range(len(arr)):
        arr[i] = arr[i] * arr[i]

    arr = sorted(arr)

    for i in range(len(arr)-1, -1, -1):
        j = 0
        k = i-1

        if arr[j] + arr[k] == arr[i]:
            return True
        elif arr[j] + arr[k] < arr[i]:
            j += 1
        else:
            k -= 1
    return False

print pythogaranTriplet([3,4,5])