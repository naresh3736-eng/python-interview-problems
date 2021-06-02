def findDuplicates(arr):
    d = {}
    for i in arr:
        if d.get(i):
            d[i] = d[i] + 1
        else:
            d[i] = 1
    print(d)
    for i in d:
        if d[i] > 1:
            print(i)

arr = [ 1, 2, 5, 1, 7, 2, 4, 2 ]
findDuplicates(arr)