implement a tree in java with descriptive comments

/**
  * A tree is a data structure that simulates a hierarchical structure,
  * with a root value and subtrees of children with a parent node,
  * represented as a set of linked nodes.
  */
public class Tree {
 
    // The root of the tree
    private Node root;
 
    /**
     * Constructs a new tree with a null root.
     */
    public Tree() {
        root = null;
    }
 
    /**
     * Constructs a new tree with the given node as its root.
     * @param root the root node
     */
    public Tree(Node root) {
        this.root = root;
    }
 
    /**
     * Returns the root node of the tree.
     * @return the root node
     */
    public Node getRoot() {
        return root;
    }
 
    /**
     * Sets the root node of the tree.
     * @param root the new root node
     */
    public void setRoot(Node root) {
        this.root = root;
    }
 
    /**
     * Returns true if the tree is empty, false otherwise.
     * @return true if the tree is empty, false otherwise
     */
    public boolean isEmpty() {
        return root == null;
    }
 
    /**
     * Returns the size of the tree, i.e. the number of nodes in the tree.
     * @return the size of the tree
     */
    public int size() {
        return isEmpty() ? 0 : root.size();
    }
 
    /**
     * Returns the height of the tree, i.e. the number of levels in the tree.
     * @return the height of the tree
     */
    public int height() {
        return isEmpty() ? 0 : root.height();
    }
 
    /**
     * Returns a string representation of the tree.
     * @return a string representation of the tree
     */
    public String toString() {
        return isEmpty() ? "()" : root.toString();
    }
 
}