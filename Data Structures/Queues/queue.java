//implement a queue in java



public class Queue {

private int[] data;

private int head;

private int tail;

private int size;

public Queue(int capacity) {

data = new int[capacity];

head = 0;

tail = 0;

size = 0;

}

public boolean isEmpty() {

return size == 0;

}

public boolean isFull() {

return size == data.length;

}

public int peek() {

if (isEmpty()) {

throw new RuntimeException("Queue is empty");

}

return data[head];

}

public void enqueue(int value) {

if (isFull()) {

throw new RuntimeException("Queue is full");

}

data[tail] = value;

tail = (tail + 1) % data.length;

size++;

}

public int dequeue() {

if (isEmpty()) {

throw new RuntimeException("Queue is empty");

}

int value = data[head];

head = (head + 1) % data.length;

size--;

return value;

}

}