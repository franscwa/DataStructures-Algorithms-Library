queue = []

def enqueue(queue, item):
    queue.append(item)

def dequeue(queue):
    if len(queue) > 0:
        item = queue.pop(0)
        return item
    else:
        print("Queue is empty!")

def peek(queue):
    if len(queue) > 0:
        return queue[0]
    else:
        print("Queue is empty!")

def isEmpty(queue):
    return len(queue) == 0

def printQueue(queue):
    for item in queue:
        print(item)