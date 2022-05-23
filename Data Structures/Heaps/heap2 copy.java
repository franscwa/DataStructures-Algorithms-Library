/*implement a heap in java with descriptive comments

A heap is a special type of binary tree in which the nodes are ordered in a specific way. The heap order property is as follows:

If A is a parent node of B then the value of A is less than or equal to the value of B.
This property must be satisfied by all nodes in the heap.

A heap can be represented by an array. The root node is stored at index 0. For any node at index i, the left child is stored at index 2i+1 and the right child is stored at index 2i+2.

The following Java code implements a max heap. The heap is represented by an array. The insert() and delete() methods are used to add and remove elements from the heap.
*/
public class Heap { 
  
    private int[] heap; 
    private int size; 
  
    public Heap(int capacity) { 
        heap = new int[capacity]; 
    } 
  
    public boolean isEmpty() { 
        return size == 0; 
    } 
  
    public int getParent(int i) { 
        return (i - 1) / 2; 
    } 
  
    public int getLeftChild(int i) { 
        return 2 * i + 1; 
    } 
  
    public int getRightChild(int i) { 
        return 2 * i + 2; 
    } 
  
    public int getMax() { 
        if (isEmpty()) 
            throw new HeapEmptyException(); 
  
        return heap[0]; 
    } 
  
    public void insert(int element) { 
        if (size == heap.length) 
            throw new HeapFullException(); 
  
        heap[size] = element; 
        size++; 
        heapifyUp(); 
    } 
  
    public int delete(int i) { 
        if (isEmpty()) 
            throw new HeapFullException(); 
  
        int deletedElement = heap[i]; 
        heap[i] = heap[size - 1]; 
        size--; 
        heapifyDown(i); 
        return deletedElement; 
    } 
  
    private void heapifyUp() { 
        int i = size - 1; 
        int element = heap[i]; 
  
        while (i > 0 && element > heap[getParent(i)]) { 
            heap[i] = heap[getParent(i)]; 
            i = getParent(i); 
        } 
  
        heap[i] = element; 
    } 
  
    private void heapifyDown(int i) { 
        int leftChild = getLeftChild(i); 
        int rightChild = getRightChild(i); 
        int largest = i; 
  
        if (leftChild < size && heap[leftChild] > heap[largest]) { 
            largest = leftChild; 
        } 
  
        if (rightChild < size && heap[rightChild] > heap[largest]) { 
            largest = rightChild; 
        } 
  
        if (largest != i) { 
            int temp = heap[i]; 
            heap[i] = heap[largest]; 
            heap[largest] = temp; 
            heapifyDown(largest); 
        } 
    } 
}