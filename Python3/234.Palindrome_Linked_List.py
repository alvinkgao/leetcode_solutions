# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if (head == None or head.next == None):
            return True
        slow = head
        fast = head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        halfway_node = self.reverseLinkedList(slow)

        while halfway_node != None:
            if head.val != halfway_node.val:
                return False
            head = head.next
            halfway_node = halfway_node.next
        return True


    def reverseLinkedList(self, head: ListNode) -> ListNode:
        prev = None
        cur = head
        next_n = None
        
        while cur != None:
            next_n = cur.next
            cur.next = prev
            prev = cur
            cur = next_n
        
        return prev;
        
        