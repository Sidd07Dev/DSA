# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        count =0
        temp=head
        while temp.next != None:
            count+=1
            temp=temp.next
        if count % 2 !=0:
            count = (int)((count/2)+1)
        else:
            count = (int)(count/2)
        temp=head
        for i in range(0,count):
           temp=temp.next
        return temp
        