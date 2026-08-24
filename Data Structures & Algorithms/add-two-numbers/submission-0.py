# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        head = dummy
        carryOver = 0
        while l1 and l2:
            val = l1.val + l2.val + carryOver
            if val > 9:
                val = val % 10
                carryOver = 1
            else: carryOver = 0
            head.next = ListNode(val)
            head = head.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            val = l1.val + carryOver
            if val > 9:
                val = val % 10
                carryOver = 1
            else: carryOver = 0
            head.next = ListNode(val)
            head = head.next
            l1 = l1.next
                    
        while l2:
            val = l2.val + carryOver
            if val > 9:
                val = val % 10
                carryOver = 1
            else: carryOver = 0
            head.next = ListNode(val)
            head = head.next
            l2 = l2.next
        if carryOver == 1:
            head.next = ListNode(carryOver)
        return dummy.next
