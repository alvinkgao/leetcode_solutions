/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
import java.util.HashSet;

public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        Set<ListNode> a_nodes = new HashSet<>();
        while (headA != null) {
            a_nodes.add(headA);
            headA = headA.next;
        }
        while (headB != null) {
            if (a_nodes.contains(headB)) {
                return headB;
            }
            headB = headB.next;
        }
        return null;
    }
}