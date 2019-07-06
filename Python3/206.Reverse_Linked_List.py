# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#iterative Solution
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        next_n = None
        while curr:
            next_n = curr.next
            curr.next = prev
            prev = curr
            curr = next_n
        return prev

#recursive Solution
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if (not head or not head.next):
            return head
        tail = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return tail