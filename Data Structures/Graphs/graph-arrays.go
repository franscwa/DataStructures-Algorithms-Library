implement a graph data structure with arrays in go

package main

import "fmt"

type graph struct {
	nodes []int
	edges [][]int
}

func (g *graph) addNode(n int) {
	g.nodes = append(g.nodes, n)
}

func (g *graph) addEdge(n1, n2 int) {
	if n1 >= len(g.edges) {
		t := make([][]int, n1+1)
		copy(t, g.edges)
		g.edges = t
	}

	g.edges[n1] = append(g.edges[n1], n2)
}

func main() {
	g := &graph{}

	g.addNode(1)
	g.addNode(2)
	g.addNode(3)
	g.addNode(4)

	g.addEdge(1, 2)
	g.addEdge(1, 3)
	g.addEdge(2, 4)
	g.addEdge(3, 4)

	fmt.Println(g.nodes)
	fmt.Println(g.edges)
}