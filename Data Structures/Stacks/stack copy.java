//implement a stack in java

public class Stack {
 
    private int[] stack;
    private int top;
 
    public Stack(int capacity) {
        stack = new int[capacity];
    }
 
    public void push(int item) {
        if (top == stack.length) {
            throw new RuntimeException("Stack is full");
        }
        stack[top++] = item;
    }
 
    public int pop() {
        if (top == 0) {
            throw new RuntimeException("Stack is empty");
        }
        return stack[--top];
    }
}