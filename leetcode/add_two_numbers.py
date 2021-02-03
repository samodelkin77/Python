# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        first = ListNode(0)
        last = first
        n = 0
        while l1 is not None or l2 is not None:
            if l1 is not None:
                n += l1.val
                l1 = l1.next
            if l2 is not None:
                n += l2.val
                l2 = l2.next
            last.next = ListNode (n % 10)
            last = last.next
            n = int (n / 10)
        if n > 0:
            last.next = ListNode (n)
        
        return first.next
       
        
        
        