from random import randint

class Node:
    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data

class LinkedList:
    countList = 0

    def __init__(self):
        self.head = None
        self.last = None

    def insert(self, new_data, index):
        new_node = Node(new_data)

        if index < 0:
            return False
        if index > self.countList:
            return False
        if index == 0 and self.head is None:
            self.head = new_node
            self.last = new_node
        elif index == 0 and self.head is not None:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        elif index == self.countList:
            new_node.prev = self.last
            self.last.next = new_node
            self.last = new_node
        else:
            current_node = self.head
            for i in range(index-1):
                current_node = current_node.next
            current_node.next.prev = new_node
            new_node.next = current_node.next
            new_node.prev = current_node
            current_node.next = new_node
        self.increment_list()
        return

    def insort(self, new_data):
        if self.head is None:
            self.insert(new_data, 0)
            return True
        if self.get_at_index(0) > new_data:
            self.insert(new_data, 0)
            return True
        for i in range(self.countList):
            if self.get_at_index(i + 1) > new_data and self.get_at_index(i) <= new_data:
                self.insert(new_data, i + 1)
                return True
        self.insert(new_data, self.countList)
        return True

    def get_at_index(self, index):
        if index > self.countList - 1:
            return float("NaN")
        if index < 0:
            return float("NaN")
        else:
            current_node = self.head
            for i in range(index):
                current_node = current_node.next
            return current_node.data

    def increment_list(self):
        self.countList += 1

    def decrement_list(self):
        self.countList -= 1

    def get_count_list(self):
        return self.countList

    def clear(self):
        self.countList = 0
        self.head = None
        self.last = None

    def remove(self, index):
        if index > self.countList - 1:
            return False
        if index < 0:
            return False
        if index == 0:
            if self.countList == 1:
                self.clear()
                return True
            else:
                self.head = self.head.next
                self.head.prev = None
        elif index == self.countList - 1:
            self.last = self.last.prev
            self.last.next = None
        else:
            current_node = self.head
            for i in range(index-1):
                current_node = current_node.next
            current_node.next.next.prev = current_node
            current_node.next = current_node.next.next
        self.decrement_list()
        return True

    def print_list(self, node):
        print("\nTraversal in forward direction")
        while node:
            print("% d" % node.data, end=' -->')
            last_node = node
            node = node.next

        print("\nTraversal in reverse direction")
        while last_node:
            print("% d" % last_node.data, end=' <--')
            last_node = last_node.prev





linked = LinkedList()

print("--- TESTING INSERT LINKED LIST --- ", end='')
# Test the insert function on 10 random numbers generated 0 - 65.
for _ in range(10):
    value = randint(0, 65)
    linked.insert(value, _)

linked.print_list(linked.head)


print('\n')
print("--- TESTING INSORT LINKED LIST --- ", end='')
linked_insort = LinkedList()
linked_insort.clear()
for _ in range(10):
    value = randint(0, 65)
    linked_insort.insort(value)
linked_insort.print_list(linked.head)




