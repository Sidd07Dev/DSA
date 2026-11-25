# class Node:
#     def __init__(self, value):
#         self.data = value  # value stored in node
#         self.next = None
#         self.prev = None

class Solution:
    def removeDuplicates(self, headRef):
        my_dict={}
        curr=headRef
        while curr:
            if curr.data in my_dict:
                curr.prev.next=curr.next
                if curr.next:
                 curr.next.prev=curr.prev
                curr= curr.next
                continue
            my_dict[curr.data]=curr
            curr= curr.next
        return headRef
            

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna