# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #function essentially makes a set and then if theres a repeat which happens
        #when there is a cycle it returns. If not retunrs false
        visited=set()
        node=head
        while node:
            if node in visited:
                return True
            visited.add(node)
            node=node.next
        return False