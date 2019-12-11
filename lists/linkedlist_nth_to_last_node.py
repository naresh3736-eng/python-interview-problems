def nth_to_last(n, head):
    left_pointer = head
    right_pointer = head

    for i in range(n-1):
        if not right_pointer.next:
            raise LookupError
        right_pointer = right_pointer.next

    while right_pointer:
        left_pointer = left_pointer.next
        right_pointer = right_pointer.next

    return left_pointer
