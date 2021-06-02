import sys
def min_max_unsorted_array(arr):
    largest = -sys.maxsize
    smallest = sys.maxsize

    for num in arr:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num
    return smallest, largest

arr = [1,5,2,4,3,8,20,2,10,10]
print(min_max_unsorted_array(arr))