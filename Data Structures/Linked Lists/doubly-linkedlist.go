//implement a doubly linked list in go



type node struct {
 
    value int
 
    next, prev *node
}
 
type List struct {
 
    head, tail *node
}
 
func (l *List) Insert(v int) {
 
    n := &node{value: v}
 
    if l.head == nil {
 
        l.head = n
    } else {
 
        l.tail.next = n
        n.prev = l.tail
    }
 
    l.tail = n
}
 
func (l *List) First() *node {
 
    return l.head
}
 
func (l *List) Last() *node {
 
    return l.tail
}
 
func (n *node) Next() *node {
 
    return n.next
}
 
func (n *node) Prev() *node {
 
    return n.prev
}