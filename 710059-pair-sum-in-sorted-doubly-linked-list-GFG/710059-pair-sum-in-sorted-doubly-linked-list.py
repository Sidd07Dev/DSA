# Structure of Doubly Linked List Node
'''
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
'''

class Solution:
    def givenSumPairs(self, head, target):
        first=head
        my_dict={}
        res=[]
        if head == None or head.next == None:
            return []
        while first:
            req=target-first.data
            if req in my_dict:
                res.append(sorted([req,first.data]))
                first=first.next
                continue
            my_dict[first.data]=first
            first=first.next
        return sorted(res)
            
            

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna