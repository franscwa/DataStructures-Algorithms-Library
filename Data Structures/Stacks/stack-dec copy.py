#implement a stack in python with descriptive comments

# a stack is a data structure that allows you to store data in a last-in, first-out (LIFO) manner.
# this means that the most recent data you have added to the stack will be the first data you remove from the stack.

# let's create a stack class to implement a stack in python

class Stack:
    # the __init__ method is called when you create a new Stack object
    # it allows you to set up the newly created object
    # in this case, we want to create an empty list to store our data
    def __init__(self):
        self.data = []

    # the push method allows you to add data to the top of the stack
    def push(self, item):
        self.data.append(item)

    # the pop method removes and returns the data from the top of the stack
    def pop(self):
        # if the stack is empty, we want to return None
        if len(self.data) == 0:
            return None
        # otherwise, we want to return the last item in the list
        return self.data.pop()

    # the peek method returns the data from the top of the stack without removing it
    def peek(self):
        # if the stack is empty, we want to return None
        if len(self.data) == 0:
            return None
        # otherwise, we want to return the last item in the list
        return self.data[-1]

    # the is_empty method returns True if the stack is empty and False if it is not
    def is_empty(self):
        return len(self.data) == 0