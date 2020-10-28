'''
Given an array A[], write a function that segragates even and odd numbers. The functions should put all even
numbers first and then odd numbers
Outpu: Print segragated array and min moves/swaps took to get the expected result
Example:
    Input = {12, 34, 45, 9, 8, 90, 3}
    Output = {12, 34, 8, 90, 45, 9, 3}
    Num of moves = 2
'''

def segregateEvenOdd(arr):
    if len(arr) == 0:
        return 0
    # initialize left and right pointers to 0 and length of the array
    left, right = 0, len(arr)-1
    count = 0

    while left < right:
        # increment left pointer while we see 0 at left
        while (arr[left] % 2 == 0 and left < right):
            left += 1

        # decrement right pointer while we see 1 at right
        while (arr[right] % 2 == 1 and left < right):
            right -= 1

        if left < right:
            # swap arrays left and right pointer positions
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
            count += 1
    # print(arr)
    return count

arr = [12, 34, 45, 9, 8, 90, 3]
print(segregateEvenOdd(arr))


