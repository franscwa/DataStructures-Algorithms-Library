//implement a circular linked list in go

type Node struct {
	Value int
	Next  *Node
}

type CircularLinkedList struct {
	Head *Node
	Tail *Node
}

func (c *CircularLinkedList) IsEmpty() bool {
	return c.Head == nil
}

func (c *CircularLinkedList) First() *Node {
	return c.Head
}

func (c *CircularLinkedList) Last() *Node {
	return c.Tail
}

func (c *CircularLinkedList) Prev(node *Node) *Node {
	if node == c.Head {
		return c.Tail
	}
	return node.Next
}

func (c *CircularLinkedList) Next(node *Node) *Node {
	if node == c.Tail {
		return c.Head
	}
	return node.Next
}

func (c *CircularLinkedList) InsertAfter(node *Node, value int) {
	newNode := &Node{Value: value, Next: c.Next(node)}
	if node == c.Tail {
		c.Tail = newNode
	}
	node.Next = newNode
}

func (c *CircularLinkedList) InsertBefore(node *Node, value int) {
	newNode := &Node{Value: value, Next: node}
	if node == c.Head {
		c.Head = newNode
	}
	c.Prev(node).Next = newNode
}

func (c *CircularLinkedList) Remove(node *Node) {
	if node == c.Head {
		c.Head = c.Next(node)
	}
	if node == c.Tail {
		c.Tail = c.Prev(node)
	}
	c.Prev(node).Next = c.Next(node)
}