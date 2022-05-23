public class BreadthFirstSearch {
 
    private Queue<Node> queue;
 
    public BreadthFirstSearch() {
        queue = new LinkedList<Node>();
    }
 
    public void bfs(Node root) {
 
        queue.add(root);
        root.visited = true;
 
        while (!queue.isEmpty()) {
 
            Node node = queue.remove();
            System.out.print(" " + node.data);
 
            Iterator<Node> i = node.neighbours.listIterator();
            while (i.hasNext()) {
                Node n = i.next();
                if (n.visited == false) {
                    queue.add(n);
                    n.visited = true;
                }
            }
        }
    }
}