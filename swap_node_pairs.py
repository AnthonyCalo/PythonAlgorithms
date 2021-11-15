# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current=head
        ended=False
        while not ended:
            if(current==None):
                ended=True
                continue
            if(current.next==None):
                ended=True
                continue
            elif(current.next.next==None):
                ended=True
            else:
                doubleNext=current.next.next
            
            singleNext=current.next
            tempVal=current.val
            current.val=singleNext.val
            singleNext.val=tempVal
            if(ended==False):
                current=doubleNext

        return head
        
            