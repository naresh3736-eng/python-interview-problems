"""
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

Example 1:

Input: head = [1,2,3,4]
Output: [2,1,4,3]
Example 2:

Input: head = []
Output: []
Example 3:

Input: head = [1]
Output: [1]
"""
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def swapPairs(head: ListNode):
    d1 = d = ListNode(0) # i/p: d->1->2->3->4 o/p: 2->1->3->4 --> 2->1->4->3
    d.next = head

    while d.next and d.next.next:
        p = d.next
        q = d.next.next
        d.next = q # d pointing to 2 in first iteration
        p.next = q.next
        q.next = p

        d = p #reset d to point to new p
    return d1.next

