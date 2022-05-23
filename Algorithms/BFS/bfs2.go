
func breadthFirstSearch(root *TreeNode) {
    // create a queue (FIFO) and enqueue the root
    queue := []*TreeNode{root}

    // continue until the queue is empty
    for len(queue) > 0 {
        // dequeue the first node in the queue
        current := queue[0]
        queue = queue[1:]

        // process the node
        fmt.Println(current.value)

        // enqueue the node's children
        for _, child := range current.children {
            queue = append(queue, child)
        }
    }
}