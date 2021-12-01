# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def max_depth(node):
            if(not node):
                return 0
            else:
                return 1 + max(max_depth(node.left), max_depth(node.right))
        if(not root):
            return True
        left_depth=max_depth(root.left)
        right_depth=max_depth(root.right)
        if(abs(left_depth-right_depth)>1):
            return False
        leftbal=self.isBalanced(root.left)
        rightbal=self.isBalanced(root.right)
		
		#if left and right are balanced, return True else return false
        if leftbal and rightbal:
            return True
        else:
            return False

'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:


Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true
 '''