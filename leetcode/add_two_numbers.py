'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution1(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        result = ListNode(0)
        restul_tail = result
        carry = 0

        while l1 or l2 or carry:
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)
            carry, out = divmod(val1 + val2 + carry, 10)

            restul_tail.next = ListNode(out)
            restul_tail = restul_tail.next

            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)

        return result.next


class Solution2:
    def addTwoNumbers(self, l1, l2):
        print(" ")
        print("inside function")

        currentCarry = 0
        head = curr = ListNode(0)

        while l1 or l2 or currentCarry:
            print(l1.val, l2.val, currentCarry)
            currentVal = currentCarry
            currentVal += 0 if l1 is None else l1.val
            currentVal += 0 if l2 is None else l2.val

            if currentVal >= 10:
                currentVal -= 10
                currentCarry = 1
            else:
                currentCarry = 0

            print(currentVal, currentCarry)

            curr.next = ListNode(currentVal)
            curr = curr.next

            if l1 is None and l2 is None:
                break
            elif l1 is None:
                l2 = l2.next
            elif l2 is None:
                l1 = l1.next
            else:
                l1 = l1.next
                l2 = l2.next

        print("exiting")
        print("")
        return head.next



# recursively print linked list

def linked_list_str(l):
    if l is None:
        return ''
    return str(l.val) + '->' +linked_list_str(l.next)
print



if __name__ == "__main__":
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    print(linked_list_str(l1))

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    print(linked_list_str(l2))

    sol1 = Solution1()
    sol2 = Solution2()
    output = sol1.addTwoNumbers(l1, l2)
    output = sol2.addTwoNumbers(l1, l2)
    print(linked_list_str(output))
