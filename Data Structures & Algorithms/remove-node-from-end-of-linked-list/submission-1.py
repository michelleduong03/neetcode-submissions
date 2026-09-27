# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        length = 0

        while curr: # O(n)
            length += 1
            curr = curr.next
        
        rmIdx = length - n

        if rmIdx == 0:
            return head.next

        curr = head
        for i in range(length - 1): # O(n)
            if (i + 1) == rmIdx:
                curr.next = curr.next.next
            curr = curr.next
        return head
