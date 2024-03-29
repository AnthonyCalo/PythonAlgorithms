# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def tree2str(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        res = ""
        def dfs(node, res):
            res += str(node.val)
            if(node.left == None and node.right != None):
                res += "()"
            if(node.left != None):
                res += "("
                res = dfs(node.left,res)
                res += ")"
            if(node.right != None):
                res += "("
                res = dfs(node.right,res)
                res += ")"
            return res
        res = dfs(root, "")
        return res
        '''
        606. Construct String from Binary Tree
Easy
2.5K
3K
Companies

Given the root of a binary tree, construct a string consisting of parenthesis and integers from a binary tree with the preorder traversal way, and return it.

Omit all the empty parenthesis pairs that do not affect the one-to-one mapping relationship between the string and the original binary tree.
        '''