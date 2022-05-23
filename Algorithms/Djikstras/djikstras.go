//implement djikstras in go with descriptive comments

package main

import (
	"container/heap"
	"fmt"
)

// A Node represents a node in the graph
type Node struct {
	name     string
	neighbors []*Node
	// The distance from the start node
	distance int
	// The priority of the node in the queue (distance + heuristic)
	priority int
	// The heuristic value of the node
	heuristic int
	// The node we came from
	previous *Node
}

// A PriorityQueue implements heap.Interface and holds Nodes.
type PriorityQueue []*Node

func (pq PriorityQueue) Len() int { return len(pq) }

func (pq PriorityQueue) Less(i, j int) bool {
	// We want Pop to give us the highest, not lowest, priority so we use greater than here.
	return pq[i].priority > pq[j].priority
}

func (pq PriorityQueue) Swap(i, j int) {
	pq[i], pq[j] = pq[j], pq[i]
	pq[i].index = i
	pq[j].index = j
}

func (pq *PriorityQueue) Push(x interface{}) {
	n := len(*pq)
	node := x.(*Node)
	node.index = n
	*pq = append(*pq, node)
}

func (pq *PriorityQueue) Pop() interface{} {
	old := *pq
	n := len(old)
	node := old[n-1]
	node.index = -1 // for safety
	*pq = old[0 : n-1]
	return node
}

// update modifies the priority and value of an Item in the queue.
func (pq *PriorityQueue) update(node *Node, distance int, heuristic int) {
	node.distance = distance
	node.heuristic = heuristic
	node.priority = distance + heuristic
	heap.Fix(pq, node.index)
}

// findNode finds a node in the graph by its name
func findNode(name string, nodes []*Node) *Node {
	for _, node := range nodes {
		if node.name == name {
			return node
		}
	}
	return nil
}

// printPath prints the path from the start node to the end node
func printPath(node *Node) {
	if node.previous != nil {
		printPath(node.previous)
	}
	fmt.Printf("%s ", node.name)
}

// Dijkstra implements Dijkstra's shortest path algorithm
func Dijkstra(start string, end string, nodes []*Node) {
	startNode := findNode(start, nodes)
	endNode := findNode(end, nodes)

	// Initialize the queue and add the start node
	pq := make(PriorityQueue, 0)
	heap.Push(&pq, startNode)

	for pq.Len() > 0 {
		// Get the node with the highest priority
		node := heap.Pop(&pq).(*Node)

		// If we've reached the end node, we're done
		if node == endNode {
			break
		}

		// Loop through the node's neighbors
		for _, neighbor := range node.neighbors {
			// Calculate the cost of reaching the neighbor
			cost := node.distance + 1

			// If the new cost is less than the neighbor's current cost, update the neighbor's cost and priority
			if cost < neighbor.distance {
				neighbor.previous = node
				pq.update(neighbor, cost, neighbor.heuristic)
			}
		}
	}

	// Print the path from start to end
	printPath(endNode)
}