def heapify(arr, n, i):
    largest = i # initialize the root as the largest
    leftchild = 2 * i + 1
    rightchild = 2 * i + 2

    # check if left child exists to root and its value is greater than the root
    if leftchild < n and arr[leftchild] > arr[i]:
        largest = leftchild

    # check if the right child to root eixsit and its value is greater than the root
    if rightchild < n and arr[rightchild] > arr[largest]:
        largest = rightchild

    # change root if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        # heapify the root
        heapify(arr, n, largest)


def heapsort(arr):
    n = len(arr)

    # build a max heap
    for i in xrange(n, -1, -1):
        heapify(arr, n, i)
        print arr, n, i

    # one by one extract elements
    for i in xrange(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

arr = [ 12, 11, 13, 5, 6, 7]
heapsort(arr)
n = len(arr)
print ("Sorted array is")
for i in range(n):
    print ("%d" %arr[i]),