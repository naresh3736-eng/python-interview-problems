def insertionSort(alist):
    for index in range(1, len(alist)):
        currentVal = alist[index]
        position = index

        while position > 0 and alist[position-1] > currentVal:
            alist[position] = alist[position-1]
            position = position - 1

        alist[position] = currentVal

    return alist

alist = [54,26,93,17,77,31,44,55,20]
print insertionSort(alist)

