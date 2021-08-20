from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class LinkedListOperations():
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current= head
        prev=None
        while(current is not None):
            next=current.next
            current.next = prev
            prev=current
            current=next
        head=prev
        return(head)
    def removeElements(self, head, val):
        current=head
        while(current!=None):
            while(current.val==val):
                if(current.next==None):
                    return(None)
                else:
                    if(current==head):
                        head=current.next
                    else:
                        current=current.next
                    

            if(current.next!=None):
                if(current.next.val==val):
                    current.next=current.next.next
                else:
                    current=current.next
            else:
                return(head)
        return(head)








