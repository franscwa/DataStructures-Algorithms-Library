//implement a circular linked list in python

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            self.head.next = self.head
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
            new_node.next = self.head

    def prepend(self, data):
        new_node = Node(data)
        cur = self.head
        new_node.next = self.head

        if self.head is None:
            new_node.next = new_node
        else:
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
        self.head = new_node

    def print_list(self):
        cur = self.head

        while cur:
            print(cur.data)
            cur = cur.next
            if cur == self.head:
                break

    def remove(self, key):
        if self.head:
            if self.head.data == key:
                if self.head == self.head.next:
                    self.head = None
                else:
                    cur = self.head
                    while cur.next != self.head:
                        cur = cur.next
                    cur.next = self.head.next
                    self.head = self.head.next
            else:
                cur = self.head
                prev = None
                while cur.next != self.head:
                    prev = cur
                    cur = cur.next
                    if cur.data == key:
                        prev.next = cur.next
                        cur = cur.next

    def __len__(self):
        cur = self.head
        count = 0
        while cur:
            count += 1
            cur = cur.next
            if cur == self.head:
                break
        return count

    def split_list(self):
        size = len(self)

        if size == 0:
            return None
        if size == 1:
            return self.head

        mid = size//2
        count = 0

        prev = None
        cur = self.head

        while cur and count < mid:
            count += 1
            prev = cur
            cur = cur.next
        prev.next = self.head

        split_cllist = CircularLinkedList()
        while cur.next != self.head:
            split_cllist.append(cur.data)
            cur = cur.next
        split_cllist.append(cur.data)

        self.print_list()
        print("\n")
        split_cllist.print_list()

    def is_circular_linked_list(self, input_list):
        if input_list.head is None:
            return True

        cur = input_list.head
        while cur.next:
            cur = cur.next
            if cur.next == input_list.head:
                return True
        return False

    def rotate(self, key):
        if self.head and self.head.next:
            p = self.head
            q = self.head
            prev = None
            count = 0
            while p and count < key:
                prev = p
                p = p.next
                q = q.next
                count += 1
            p = prev
            while q:
                prev = q
                q = q.next
                if q == self.head:
                    break
            q = prev
            self.head = p.next
            p.next = self.head
            q.next = self.head

    def josephus_circle(self, step):
        cur = self.head

        while len(self) > 1:
            count = 1
            while count != step:
                cur = cur.next
                count += 1
            print("REMOVED: " + str(cur.data))
            self.remove(cur.data)
            cur = cur.next

    def is_empty(self):
        if self.head:
            return False
        else:
            return True

    def is_palindrome(self):
        s = ""
        cur = self.head
        while cur:
            s += cur.data
            cur = cur.next
            if cur == self.head:
                break
        return s == s[::-1]

cllist = CircularLinkedList()
cllist.append("A")
cllist.append("B")
cllist.append("C")
cllist.append("D")
cllist.append("E")
cllist.append("F")

cllist.prepend("G")

# cllist.remove("B")
# cllist.remove("C")
# cllist.remove("F")

# cllist.rotate(3)

# cllist.josephus_circle(2)

# print(cllist.is_empty())
# print(cllist.is_palindrome())

# print(len(cllist))

# cllist.print_list()

# cllist.split_list()

# print(cllist.is_circular_linked_list(cllist))