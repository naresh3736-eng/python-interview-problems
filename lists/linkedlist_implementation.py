class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node()

    def add(self, data):
        new_node = Node(data)
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
        current_node.next = new_node

    def size(self):
        current_node = self.head
        count = 0
        while current_node.next != None:
            count += 1
            current_node = current_node.next
        return count

    def display(self):
        elements = []
        cureent_node = self.head
        while cureent_node.next != None:
            cureent_node = cureent_node.next
            elements.append(cureent_node.data)

    def get(self, index):
        if index>=self.size():
            print 'Error, Index out of range'
            return None
        curr_idx = 0
        current_node = self.head
        while True:
            current_node = current_node.next
            if curr_idx == index:
                return current_node.data
            curr_idx += 1

    def remove(self, index):
        if index>= self.size():
            print 'Error, Index out of range'
            return None
        curr_idx = 0
        current_node = self.head
        while True:
            previous_node = current_node
            current_node = current_node.next
            if curr_idx == index:
                previous_node.next = current_node.next
                return
            curr_idx += 1

mylist = LinkedList()
mylist.display()

mylist.add(1)
mylist.add(2)
mylist.display()