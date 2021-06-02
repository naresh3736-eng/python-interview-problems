# using doubly linked list and dict

class DLLNode():
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.next = None
        self.prev = None

class LRUCache():
    def __init__(self, capacity=None):
        self.capacity = capacity
        self.length = 0
        self.cache = {}
        self.head = DLLNode(-1, -1)
        self.tail = self.head

    def get(self, key) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        val = node.val
        while node.next:
            node.prev.next = node.next
            node.next.prev = node.prev
            self.tail.next = node
            node.prev = self.tail
            node.next = None
            self.tail = node
        return val

    def put(self, key, value) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            while node.next:
                node.prev.next = node.next
                node.next.prev = node.prev
                self.tail.next = node
                node.prev = self.tail
                node.next = None
                self.tail = node
        else:
            node = DLLNode(key, value)
            self.cache[key] = node
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            self.length += 1
            if self.length > self.capacity:
                remove = self.head.next
                self.head.next = self.head.next.next
                self.head.next.prev = self.head
                del self.cache[remove.key]
                self.length -= 1

