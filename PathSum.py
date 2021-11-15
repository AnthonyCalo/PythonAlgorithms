# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        su=0
        def dfs(root=root, su=0):
            if(not root):
                return False
            su+=root.val
            if not (root.left or root.right) and su == targetSum:
                return True
            #returning if either of those are true. hence the or
            return(dfs(root.left, su)or dfs(root.right, su)) 
        return dfs()
            
            