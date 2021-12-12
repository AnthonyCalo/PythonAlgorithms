# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        acount=0
        bcount=0
        cura, curb=headA, headB
        while cura:
            acount+=1
            cura=cura.next
        while curb:
            bcount+=1
            curb=curb.next
        cura, curb= headA, headB
        if(bcount>acount):
            for i in range(bcount-acount):
                curb=curb.next
        elif(acount>bcount):
            for i in range(acount-bcount):
                cura=cura.next
        #the algorithm basically makes the lists the same length.
        #then returns after they are both equal to each other
        while cura!=curb:
            cura=cura.next
            curb=curb.next
        return cura
                
        