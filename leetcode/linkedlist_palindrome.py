'''
Given the head of a singly linked list, return true if it is a palindrome.

Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false

Solution:
initialize two pointers m1 and m2 pointing to head
move m1 one step forward and m2 two steps forward until we reach mid of the list (i.e. until m2 is not None and m2.next is not None)
As moving forward stack the m1 node values (i.e. push half of the list node values into stack)
For odd lenght list move slow one step a head for further comparison with right half of the given list
In case of even length continue with the rest of the comparison with right half of the given list
To compare, loop until m1 is not None and len(stack) is not zero and pop the stack and compare it with m1 value and if not equals return False else return True
'''

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def linkedListPalindrome(head: ListNode):
    if head is None:
        return True
    marker1 = marker2 = head
    stack = []

    while marker2 and marker2.next:
        stack.append(marker1.val)
        marker1 = marker1.next
        marker2 = marker2.next.next

    if marker2: # in case of odd length
        marker1 = marker1.next
    while marker1 and len(stack):
        if stack.pop() != marker1.val:
            return False
        marker1 = marker1.next
    return True


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(1)

print(linkedListPalindrome(head))