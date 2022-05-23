/*
1.  Define a function that takes in a graph and a starting node
2.  Create a list to keep track of visited nodes
3.  Create a stack to keep track of nodes to visit
4.  Add the starting node to the stack
5.  While the stack is not empty:
6.  Pop the first node off the stack
7.  If the node has not been visited:
8.  Mark the node as visited
9.  Add the node's neighbors to the stack
10. Return the list of visited nodes
*/

program depth first search in go with descriptive comments



package main

import "fmt"

// Node in a tree
type Node struct {
	// left and right child nodes
	left, right *Node
	// value stored at this node
	value int
}

// NewNode creates a new Node
func NewNode(value int) *Node {
	return &Node{nil, nil, value}
}

// SetLeftChild assigns a left child to a Node
func (n *Node) SetLeftChild(child *Node) {
	n.left = child
}

// SetRightChild assigns a right child to a Node
func (n *Node) SetRightChild(child *Node) {
	n.right = child
}

// DepthFirstSearch performs a depth first search on a tree
// starting at the given root Node
func DepthFirstSearch(root *Node) {
	// create a stack to store nodes
	var stack []*Node
	// push the root node onto the stack
	stack = append(stack, root)
	// continue until the stack is empty
	for len(stack) > 0 {
		// pop the top node off the stack
		curr := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		// print the value stored at the node
		fmt.Println(curr.value)
		// push the node's right child onto the stack
		if curr.right != nil {
			stack = append(stack, curr.right)
		}
		// push the node's left child onto the stack
		if curr.left != nil {
			stack = append(stack, curr.left)
		}
	}
}

func main() {
	// create a tree
	//          1
	//        /   \
	//       2     3
	//      / \   / \
	//     4   5 6   7
	root := NewNode(1)
	root.SetLeftChild(NewNode(2))
	root.SetRightChild(NewNode(3))
	root.left.SetLeftChild(NewNode(4))
	root.left.SetRightChild(NewNode(5))
	root.right.SetLeftChild(NewNode(6))
	root.right.SetRightChild(NewNode(7))
	// perform depth first search
	DepthFirstSearch(root)
}