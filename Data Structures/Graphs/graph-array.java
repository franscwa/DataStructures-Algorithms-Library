package java;

public class graph-array {
    
}

public class Graph {

    private int[][] edges;
    
    private int numVertices;
    
    public Graph(int numVertices) {
    
    this.numVertices = numVertices;
    
    edges = new int[numVertices][numVertices];
    
    }
    
    public void addEdge(int from, int to) {
    
    edges[from][to] = 1;
    
    }
    
    public boolean hasEdge(int from, int to) {
    
    return edges[from][to] == 1;
    
    }
    
    public int getNumVertices() {
    
    return numVertices;
    
    }
    
    public int[] getNeighbors(int vertex) {
    
    int[] neighbors = new int[numVertices];
    
    int index = 0;
    
    for (int i=0; i<numVertices; i++) {
    
    if (edges[vertex][i] == 1) {
    
    neighbors[index++] = i;
    
    }
    
    }
    
    return neighbors;
    
    }
    
    }