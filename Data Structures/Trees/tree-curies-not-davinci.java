import java.util.ArrayList; import java.util.List; public class Tree { 
    private ArrayList<Integer> numbers;
     private List<Integer> leaves; 
     public Tree(ArrayList<Integer> numbers, List<Integer> leaves) 
     { this.numbers = numbers; this.leaves = leaves; 
    } public Integer getNodeNumber(Integer root)
     { return numbers.get(root); } 
     public void addNode(Integer number) 
     { numbers.add(number); 
        leaves.add(number); }
         public void deleteNode(Integer number)
          { if (numbers.isEmpty())
             { numbers.clear(); }
              else 
              { if (leaves.isEmpty())
                 { leaves.clear(); }
                  else 
                  { Integer left = numbers.get(numbers.size()-1); 
                    Integer right = numbers.get(numbers.size()-1); 
                    if (left > right)
                     { numbers.remove(left); leaves.remove(right); } }
                     } } public void printNodeInfo(Integer number)
                      { System.out.println("Node number: " + number);
                       System.out.println("Leaf number: " + leaves.get(number)); } }