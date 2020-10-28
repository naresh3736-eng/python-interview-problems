# Divide and Conquer Method
# for Linked Lists TC O(nlog(k)) and SC O(1)
# for Lists TC O9nlog(k)) and SC O(n)

class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# utility function to print result
def printList(node):
    while node:
        #print(node.data, end="->")
        print
        node = node.next
    print("None")

# method to take two lists and merge them
def mergeSortedLists(a, b):
    if a is None:
        return b
    if b is None:
        return a

    if a.data <= b.data:
        result = a
        result.next = mergeSortedLists(a.next, b)
    else:
        result = b
        result.next = mergeSortedLists(a, b.next)
    return result


# main to merge sorted lists
def mergeKList(A, k):
    last = k - 1
    while last:
        (i, j) = (0, last)
        while i < j:
            # merge lists i j and store output in list i
            A[i] = mergeSortedLists(A[i], A[j])

            # consider next pair
            i = i + 1
            j = j - 1

            if i>=j:
                last = j
    return A[0]


if __name__ == "__main__":
    k = 3
    A = [Node] * k
    A[0] = Node(1)
    A[0].next = Node(5)
    A[0].next.next = Node(7)

    A[1] = Node(2)
    A[1].next = Node(3)
    A[1].next.next = Node(6)
    A[1].next.next.next = Node(9)

    A[2] = Node(4)
    A[2].next = Node(8)
    A[2].next.next = Node(10)

    head = mergeKList(A, k)