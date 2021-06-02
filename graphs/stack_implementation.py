class Stack():
    def __init__(self, capacity):
        self.stack = list()
        self.capacity = capacity

    def size(self):
        return len(self.stack)

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, item):
        if self.size() >= self.capacity:
            return Exception("Stack is Full")
        self.stack.append(item)

    def pop(self):
        if self.isEmpty():
            return "Stack is Empty"
        return self.stack.pop()

if __name__ == "__main__":
    s = Stack(5)
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.pop())
    print(s.pop())
    print(s.pop())