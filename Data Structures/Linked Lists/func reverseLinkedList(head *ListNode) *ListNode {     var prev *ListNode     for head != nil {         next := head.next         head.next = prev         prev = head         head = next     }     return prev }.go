//This is a basic implementation of a linked list in Go. It is a singly linked list, which means that each node only has a reference to the next node in the list.

type Node struct {
	data int
	next *Node
}

func (n *Node) AddToList(data int) {
	if n.next == nil {
		n.next = &Node{data: data}
	} else {
		n.next.AddToList(data)
	}
}

func (n *Node) PrintList() {
	if n.next == nil {
		fmt.Println(n.data)
	} else {
		fmt.Println(n.data)
		n.next.PrintList()
	}
}
func reverseLinkedList(head *ListNode) *ListNode {
    var prev *ListNode
    for head != nil {
        next := head.next
        head.next = prev
        prev = head
        head = next
    }
    return prev
}