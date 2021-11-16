# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(p=p, q=q):
            #if one value is null return false
            if(p and not q):
                return False
            elif(q and not p):
                return False
            #if both are null return true
            elif not (p and q):
                return True
            if(p.val==q.val):
                #return true if both left and right are equal
                return(dfs(p.left, q.left) and dfs(p.right, q.right))
            else:
                return False
            
        return(dfs())