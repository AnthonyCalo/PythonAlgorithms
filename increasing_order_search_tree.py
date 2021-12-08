# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
#         arr=list()
        
#         def in_order(root,arr):
#             if root:
#                 in_order(root.left,arr)
#                 arr.append(root.val)
#                 in_order(root.right,arr)
#         in_order(root, arr) 
        node_list=[]
        def dfs(node):
            if not node:
                return
            node_list.append(node.val)
            dfs(node.right)
            dfs(node.left)
        dfs(root)
        node_list.sort()
        # node_list=node_list.sort()
        ret = TreeNode()
        root=ret
        for i in node_list:
            root.right=TreeNode(i)
            root=root.right
        return(ret.right)


        '''Given the root of a binary search tree,
        . rearrange the tree in in-order so that the left
        most node in the tree is now the root of the tree,
         and every node has no left child and only one right child.'''