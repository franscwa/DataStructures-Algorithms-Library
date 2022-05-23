//implement depth-first search in java

public class DepthFirstSearch { 
  
    // A utility function to print the adjacency list 
    // representation of graph 
    static void printGraph(ArrayList<ArrayList<Integer>> adj) 
    { 
        for (int i = 0; i < adj.size(); i++) { 
            System.out.println("Adjacency list of vertex" + i); 
            System.out.print(" head"); 
            for (int j = 0; j < adj.get(i).size(); j++) { 
                System.out.print(" -> "+adj.get(i).get(j)); 
            } 
            System.out.println("\n"); 
        } 
    } 
  
    // Driver code 
    public static void main(String args[]) 
    { 
        // Create a graph given in the above diagram 
        int V = 5; 
        ArrayList<ArrayList<Integer>> adj = new ArrayList<ArrayList<Integer>>(V); 
  
        for (int i = 0; i < V; i++) 
            adj.add(new ArrayList<Integer>()); 
  
        addEdge(adj, 0, 1); 
        addEdge(adj, 0, 4); 
        addEdge(adj, 1, 2); 
        addEdge(adj, 1, 3); 
        addEdge(adj, 1, 4); 
        addEdge(adj, 2, 3); 
        addEdge(adj, 3, 4); 
  
        // print the adjacency list representation of 
        // the above graph 
        printGraph(adj); 
    } 
}