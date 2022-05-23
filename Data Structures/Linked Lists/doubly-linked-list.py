implement a doubly linked list in python

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0

    def add_first(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.num_elements += 1

    def add_last(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.num_elements += 1

    def add_at_index(self, index, data):
        if index > self.num_elements:
            return
        elif index == self.num_elements:
            self.add_last(data)
        elif index == 0:
            self.add_first(data)
        else:
            current = self.head
            for i in range(index - 1):
                current = current.next
            new_node = Node(data)
            new_node.next = current.next
            new_node.prev = current
            current.next = new_node
            self.num_elements += 1

    def remove_first(self):
        if self.is_empty():
            return
        self.head = self.head.next
        self.head.prev = None
        self.num_elements -= 1

    def remove_last(self):
        if self.is_empty():
            return
        self.tail = self.tail.prev
        self.tail.next = None
        self.num_elements -= 1

    def remove_at_index(self, index):
        if index >= self.num_elements:
            return
        elif index == 0:
            self.remove_first()
        elif index == self.num_elements - 1:
            self.remove_last()
        else:
            current = self.head
            for i in range(index):
                current = current.next
            current.prev.next = current.next
            current.next.prev = current.prev
            self.num_elements -= 1

    def get_first(self):
        if self.is_empty():
            return None
        return self.head.data

    def get_last(self):
        if self.is_empty():
            return None
        return self.tail.data

    def get_at_index(self, index):
        if index >= self.num_elements:
            return None
        current = self.head
        for i in range(index):
            current = current.next
        return current.data

    def clear(self):
        self.head = None
        self.tail = None
        self.num_elements = 0

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


    def reverse_list(self):
        temp = self.head
        self.tail = self.head
        prev = None
        while temp:
            next = temp.next
            temp.next = prev
            temp.prev = next
            prev = temp
            temp = next
        self.head = prev

my_list = DoublyLinkedList()
my_list.add_first(5)
my_list.add_first(15)
my_list.add_last(25)
my_list.add_last(35)
my_list.add_at_index(2, 20)
my_list.print_list()
print("\n")
my_list.reverse_list()
my_list.print_list()
# 15 5 20 25 35