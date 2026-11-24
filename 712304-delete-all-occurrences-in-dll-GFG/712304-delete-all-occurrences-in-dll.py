# Structure of the doubly linked list Node 
# class Node:
#     def __init__(self, x):
#         self.data = x
#         self.next = None
#         self.prev = None

class Solution:
    def deleteAllOccurOfX(self, head, x):
        # code here
        curr=head
        while curr:
            prev=curr.prev
            next_=curr.next
            if curr == head and curr.data == x:
               head=next_
               curr=next_
               continue
            if curr.data == x:
                if prev != None:
                  prev.next=next_
                if next_ != None:
                 next_.prev=prev
            
            curr=next_
        return head

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna