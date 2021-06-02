class QueueUsingStack():
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack1 = self.stack2 = list()

    def size(self):
        return len(self.stack1) + len(self.stack2)

    def enqueue(self, item):
        self.stack1.append(item)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

