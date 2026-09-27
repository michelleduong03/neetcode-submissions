# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        val = []

        while list1:
            val.append(list1.val)
            list1 = list1.next
        
        while list2:
            val.append(list2.val)
            list2 = list2.next

        val.sort()

        tmp = ListNode()

        curr = tmp

        for i in val:
            curr.next = ListNode(i)
            curr = curr.next
        
        return tmp.next