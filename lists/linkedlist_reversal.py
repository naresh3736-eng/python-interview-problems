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

