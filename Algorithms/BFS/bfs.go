//implement breadth-first search in go with descriptive comments

package main

import "fmt"

// Node type for a tree
type Node struct {
	Value int
	Left  *Node
	Right *Node
}

// Tree type
type Tree struct {
	Root *Node
}

// BFS function definition
func (t *Tree) BFS() {
	if t.Root == nil {
		return
	}

	queue := []*Node{t.Root}

	for len(queue) > 0 {
		node := queue[0]
		queue = queue[1:]

		fmt.Println(node.Value)

		if node.Left != nil {
			queue = append(queue, node.Left)
		}
		if node.Right != nil {
			queue = append(queue, node.Right)
		}
	}
}

func main() {
	tree := &Tree{}
	tree.Root = &Node{Value: 1}
	tree.Root.Left = &Node{Value: 2}
	tree.Root.Right = &Node{Value: 3}
	tree.Root.Left.Left = &Node{Value: 4}
	tree.Root.Left.Right = &Node{Value: 5}

	tree.BFS()
}