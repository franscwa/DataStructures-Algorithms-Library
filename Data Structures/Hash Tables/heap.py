#implement a heap in python

class Heap:
    def __init__(self):
        self.heap_array = []
 
    def insert(self, k):
        self.heap_array.append(k)
 
    def sift_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.heap_array[index] < self.heap_array[parent]:
                self.heap_array[index], self.heap_array[parent] = self.heap_array[parent], self.heap_array[index]
                index = parent
            else:
                break
 
    def get_min(self):
        if self.heap_array:
            return self.heap_array[0]
 
    def sift_down(self, index):
        min_index = index
        left = 2 * index + 1
        right = 2 * index + 2
 
        if left < len(self.heap_array) and self.heap_array[left] < self.heap_array[min_index]:
            min_index = left
 
        if right < len(self.heap_array) and self.heap_array[right] < self.heap_array[min_index]:
            min_index = right
 
        if min_index != index:
            self.heap_array[index], self.heap_array[min_index] = self.heap_array[min_index], self.heap_array[index]
            self.sift_down(min_index)
 
    def extract_min(self):
        if self.heap_array:
            min_elem = self.heap_array[0]
            self.heap_array[0] = self.heap_array[-1]
            del self.heap_array[-1]
            self.sift_down(0)
            return min_elem
 
    def heapify(self, array):
        self.heap_array = array
        for i in range((len(array) - 2) // 2, -1, -1):
            self.sift_down(i)