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

'''
intutive approach where we append all the list of list elements into a new list and sort it. This approach
takes extra space
'''

def intuitiveApproach(lists: list):
    res = []
    dummy = head = Node(0)
    for l in lists:
        while l:
            res.append(l.val)
            l = l.next
    for x in sorted(res):
        dummy.next = Node(x)
        dummy = dummy.next
    return head.next


'''
efficient solution to above using merge sort
'''

def merge(l1: Node, l2: Node):
    curr = dummy = Node(0)
    while l1 and l2:
        if l1.data <= l2.data:
            curr.next = Node(l1.data)
            curr = curr.next
            l1 = l1.next
        else:
            curr.next = Node(l2.data)
            curr = curr.next
            l2 = l2.next
    if l1:
        curr.next = l1
    else:
        curr.next = l2

    '''
    while l1:
        curr.next = Node(l1.val)
        curr = curr.next
        l1 = l1.next
    while l2:
        curr.next = Node(l2.val)
        curr = curr.next
        l2 = l2.next
    '''
    return dummy.next

def mergeKlists(lists: list):
    if not lists:
        return
    if len(lists) == 1:
        return lists[0]
    mid = len(lists)//2
    l = mergeKlists(lists[:mid])
    r = mergeKlists(lists[mid:])
    return merge(l, r)