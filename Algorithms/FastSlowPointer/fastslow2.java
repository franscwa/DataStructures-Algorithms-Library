public class FastSlowPointer {

    public static ListNode findCycleStart(ListNode head) {
        ListNode slow = head, fast = head;

        while (fast != null && fast.next != null) {
            slow = slow.next;           //slow pointer moves one step at a time
            fast = fast.next.next;      //fast pointer moves two steps at a time

            if (slow == fast) {        //they meet when there is a cycle
                break;
            }
        }

        if (fast == null || fast.next == null) {    //no cycle
            return null;
        }

        slow = head;
        while (slow != fast) {                    //both pointers move one step at a time until they meet at the start of the cycle
            slow = slow.next;
            fast = fast.next;
        }

        return fast;
    }

    public static void main(String[] args) {
        ListNode head = new ListNode(1);
        head.next = new ListNode(2);
        head.next.next = new ListNode(3);
        head.next.next.next = new ListNode(4);
        head.next.next.next.next = new ListNode(5);
        head.next.next.next.next.next = new ListNode(6);

        head.next.next.next.next.next.next = head.next.next;
        System.out.println("LinkedList cycle start: " + FastSlowPointer.findCycleStart(head).value);

        head.next.next.next.next.next.next = head.next.next.next;
        System.out.println("LinkedList cycle start: " + FastSlowPointer.findCycleStart(head).value);

        head.next.next.next.next.next.next = head;
        System.out.println("LinkedList cycle start: " + FastSlowPointer.findCycleStart(head).value);
    }
}

class ListNode {
    int value = 0;
    ListNode next;

    ListNode(int value) {
        this.value = value;
    }
}

//O(n) time and O(1) space
//fast and slow pointers are used to find the start of a cycle in a linked list
//if the fast pointer catches up to the slow pointer, then there is a cycle
//once they meet, move the slow pointer to the head and keep the fast pointer where it is
//move both pointers one step at a time until they meet again, this time they will be at the start of the cycle