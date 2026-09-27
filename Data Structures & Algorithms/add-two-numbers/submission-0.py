# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        temp = result

        while l1 != None or l2 != None:
            total = 0
            carry = 0

            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            
            total += temp.val

            if total > 9:
                carry = int(total/10)
                total %= 10

            temp.val = total

            if not carry and not l1 and not l2:
                return result

            temp.next = ListNode()
            temp = temp.next
            temp.val = carry
        return result



