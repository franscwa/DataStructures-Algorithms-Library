implement a heap in python with descriptive comments

A heap is a data structure that allows efficient retrieval and removal of the maximum element. Heaps are often implemented with an array.

In a max heap, each node has a value greater than or equal to the values of its children. The root node has the maximum value in the heap.

A min heap is similar, but each node has a value less than or equal to the values of its children. The root node has the minimum value in the heap.

Heaps are used in a variety of applications, including priority queues, heapsort, and graph traversal algorithms.

# max heap
class MaxHeap:
    def __init__(self):
        self.heap = []
 
    def insert(self, val):
        self.heap.append(val)
        self.percolate_up()
 
    def percolate_up(self):
        idx = len(self.heap) - 1
        while idx > 0:
            parent_idx = (idx - 1) // 2
            if self.heap[idx] > self.heap[parent_idx]:
                self.heap[idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[idx]
                idx = parent_idx
            else:
                break
 
    def remove_max(self):
        if self.heap:
            self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
            max_val = self.heap.pop()
            self.percolate_down()
            return max_val
 
    def percolate_down(self):
        idx = 0
        while idx < len(self.heap):
            left_child_idx = 2 * idx + 1
            right_child_idx = 2 * idx + 2
            if left_child_idx >= len(self.heap):
                break
            elif right_child_idx >= len(self.heap):
                if self.heap[idx] < self.heap[left_child_idx]:
                    self.heap[idx], self.heap[left_child_idx] = self.heap[left_child_idx], self.heap[idx]
                    idx = left_child_idx
                else:
                    break
            else:
                if self.heap[left_child_idx] > self.heap[right_child_idx]:
                    if self.heap[idx] < self.heap[left_child_idx]:
                        self.heap[idx], self.heap[left_child_idx] = self.heap[left_child_idx], self.heap[idx]
                        idx = left_child_idx
                    else:
                        break
                else:
                    if self.heap[idx] < self.heap[right_child_idx]:
                        self.heap[idx], self.heap[right_child_idx] = self.heap[right_child_idx], self.heap[idx]
                        idx = right_child_idx
                    else:
                        break
 
    def peek_max(self):
        if self.heap:
            return self.heap[0]
 

# min heap
class MinHeap:
    def __init__(self):
        self.heap = []
 
    def insert(self, val):
        self.heap.append(val)
        self.percolate_up()
 
    def percolate_up(self):
        idx = len(self.heap) - 1
        while idx > 0:
            parent_idx = (idx - 1) // 2
            if self.heap[idx] < self.heap[parent_idx]:
                self.heap[idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[idx]
                idx = parent_idx
            else:
                break
 
    def remove_min(self):
        if self.heap:
            self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
            min_val = self.heap.pop()
            self.percolate_down()
            return min_val
 
    def percolate_down(self):
        idx = 0
        while idx < len(self.heap):
            left_child_idx = 2 * idx + 1
            right_child_idx = 2 * idx + 2
            if left_child_idx >= len(self.heap):
                break
            elif right_child_idx >= len(self.heap):
                if self.heap[idx] > self.heap[left_child_idx]:
                    self.heap[idx], self.heap[left_child_idx] = self.heap[left_child_idx], self.heap[idx]
                    idx = left_child_idx
                else:
                    break
            else:
                if self.heap[left_child_idx] < self.heap[right_child_idx]:
                    if self.heap[idx] > self.heap[left_child_idx]:
                        self.heap[idx], self.heap[left_child_idx] = self.heap[left_child_idx], self.heap[idx]
                        idx = left_child_idx
                    else:
                        break
                else:
                    if self.heap[idx] > self.heap[right_child_idx]:
                        self.heap[idx], self.heap[right_child_idx] = self.heap[right_child_idx], self.heap[idx]
                        idx = right_child_idx
                    else:
                        break
 
    def peek_min(self):
        if self.heap:
            return self.heap[0]