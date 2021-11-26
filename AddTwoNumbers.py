# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1=""
        n2=""
        while l1:
            n1=n1 + str(l1.val)
            l1=l1.next
        while l2:
            n2=n2 + str(l2.val)
            l2=l2.next
        if not n1: n1="0"
        if not n2: n2="0"
        n1=n1[::-1]
        n2=n2[::-1]
        
        summ=int(n1)+int(n2)
        
        head=cur=ListNode()
        for i in reversed(str(summ)):
            cur.next=ListNode(int(i))
            cur=cur.next
        return(head.next)
        

        '''
        You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
        '''