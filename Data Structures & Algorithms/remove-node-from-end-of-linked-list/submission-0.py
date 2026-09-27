# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []
        tmp = head

        while tmp:
            nodes.append(tmp)
            tmp = tmp.next
        
        rmIdx = len(nodes) - n

        if rmIdx == 0:
            return head.next
        
        nodes[rmIdx - 1].next = nodes[rmIdx].next
        return head