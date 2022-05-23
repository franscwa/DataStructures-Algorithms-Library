#implement a queue in python with descriptive comments

#A queue is a data structure that stores items in a First-In-First-Out (FIFO) manner.

#!/usr/bin/env python

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)