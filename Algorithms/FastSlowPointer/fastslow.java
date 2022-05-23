/**
 * Fast slow pointer is a technique used to find the middle element of a singly linked list in one pass.
 * The idea is to use two pointers, one slow pointer and one fast pointer. The slow pointer moves one node at a time while the fast pointer moves two nodes at a time.
 * When the fast pointer reaches the end of the list, the slow pointer will be at the middle of the list.
 */

public class FastSlowPointer {
    
    public static ListNode findMiddle(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;
        
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        
        return slow;
    }
    
}