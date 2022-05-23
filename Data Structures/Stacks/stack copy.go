//implement a stack in go

package main

type Stack struct {
	// create a slice of ints to store our stack
	data []int
}

// Stack constructor function
func NewStack() *Stack {
	// initialize our Stack
	return &Stack{}
}

// Push a new item onto the stack
func (s *Stack) Push(item int) {
	// append the item to the end of the stack
	s.data = append(s.data, item)
}

// Pop an item off the stack
func (s *Stack) Pop() int {
	// get the length of the stack
	l := len(s.data)
	// if the stack is empty, return nil
	if l == 0 {
		return nil
	}
	// get the last item on the stack
	item := s.data[l-1]
	// remove the last item from the stack
	s.data = s.data[:l-1]
	// return the item
	return item
}