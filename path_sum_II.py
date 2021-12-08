# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ret=[]
        def dfs_sum(node, summ, path=[]):
            mypath=path.copy()
            if( not node ):
                return
            mypath.append(node.val)
            summ+=node.val
            if(summ==targetSum):
                if(not node.left and not node.right):
                    ret.append(mypath)
                    return
            dfs_sum(node.left, summ, mypath)
            dfs_sum(node.right, summ, mypath)

        dfs_sum(root, 0)
        return(ret)


'''
DFS based solution. Function calls itself on each node while adding node
to the summ. if the summ equals the target and its a leaf then
it adds that path to return list.


Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

 
'''
                