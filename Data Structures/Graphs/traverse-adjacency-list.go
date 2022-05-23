//traverse a graph adjacency list in go
/*
in order traversal graph in go

1.  Create a new graph
2.  Add the root node to the graph
3.  While there are nodes in the graph:
4.  Find the node with the smallest value
5.  Visit the left child of the node
6.  Visit the right child of the node
7.  Remove the node from the graph
*/
package main

import "fmt"

type Node struct {
	value int
	next  *Node
}

func (n *Node) Traverse() {
	if n == nil {
		return
	}
	curr := n
	for curr != nil {
		fmt.Println(curr.value)
		curr = curr.next
	}
}

func main() {
	n1 := &Node{1, nil}
	n2 := &Node{2, nil}
	n3 := &Node{3, nil}

	n1.next = n2
	n2.next = n3

	n1.Traverse()
}