class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Reversal:
    def reverse(selfs, head):
        previous = None

        while head:
            temp = head
            head = head.next
            temp.next = previous
            previous = temp

        return previous

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
rev = Reversal()
res = rev.reverse(head)

while res:
    print(res.data, end='->')
    res = res.next

