implement a graph with an adjacency list in go

package main

import "fmt"

type Graph struct {
    // we'll use a map to store our adjacency list
    adjacencyList map[string][]string
}

// add a new vertex to the graph
func (g *Graph) AddVertex(vertex string) {
    // if our graph's adjacency list hasn't been initialized yet, do so
    if g.adjacencyList == nil {
        g.adjacencyList = make(map[string][]string)
    }
    // add our vertex to the adjacency list, init its values to an empty slice
    g.adjacencyList[vertex] = make([]string, 0)
}

// add a new edge to the graph
func (g *Graph) AddEdge(fromVertex string, toVertex string) {
    // if our graph's adjacency list hasn't been initialized yet, do so
    if g.adjacencyList == nil {
        g.adjacencyList = make(map[string][]string)
    }
    // if the vertex doesn't exist in our adjacency list, add it
    if _, exists := g.adjacencyList[fromVertex]; !exists {
        g.AddVertex(fromVertex)
    }
    // if the vertex doesn't exist in our adjacency list, add it
    if _, exists := g.adjacencyList[toVertex]; !exists {
        g.AddVertex(toVertex)
    }
    // add the edge
    g.adjacencyList[fromVertex] = append(g.adjacencyList[fromVertex], toVertex)
}

// print out the graph
func (g *Graph) String() {
    // if our graph's adjacency list hasn't been initialized yet, do so
    if g.adjacencyList == nil {
        g.adjacencyList = make(map[string][]string)
    }
    fmt.Println("Adjacency List:")
    for key, value := range g.adjacencyList {
        fmt.Println(key, "->", value)
    }
}

func main() {
    // create a new graph
    g := &Graph{}
    // add some vertices
    g.AddVertex("A")
    g.AddVertex("B")
    g.AddVertex("C")
    g.AddVertex("D")
    g.AddVertex("E")
    g.AddVertex("F")
    // add some edges
    g.AddEdge("A", "B")
    g.AddEdge("A", "C")
    g.AddEdge("B", "D")
    g.AddEdge("C", "E")
    g.AddEdge("D", "E")
    g.AddEdge("D", "F")
    g.AddEdge("E", "F")
    // print out the graph
    fmt.Println(g)
}