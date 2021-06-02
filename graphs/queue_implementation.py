class Queue():
    def __init__(self, capacity):
        self.queue = list()
        self.capacity = capacity

    def size(self):
        return len(self.queue)

    def isEmpty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        if self.size() >= self.capacity:
             raise Exception("Queue is Full")

        self.queue.append(item)

    def dequeue(self):
        return self.queue.pop(0)

if __name__ == "__main__":
    q = Queue(5)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    print(q.queue)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())


