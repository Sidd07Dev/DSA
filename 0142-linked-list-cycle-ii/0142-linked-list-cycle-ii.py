# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head
        my_set=[]
        while fast and fast.next:
            if slow in my_set:
                return slow
            my_set.append(slow)
            fast = fast.next.next
            slow = slow.next

            

        