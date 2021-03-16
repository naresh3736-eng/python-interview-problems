from random import randint
def quickSort(alist):
    if len(alist) <= 1:
        return alist

    smaller, equal, larger = [], [], []

    pivot = alist[randint(0, len(alist)-1)]

    for item in alist:
        if item < pivot:
            smaller.append(item)
        elif item == pivot:
            equal.append(item)
        else:
            larger.append(item)

    return quickSort(smaller) + equal + quickSort(larger)

nlist = [54,26,93,17,77,31,44,55,20]
print(quickSort(nlist))