"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        mydict = dict()
        if not node:
            return
        def dfs(node):
            if( node in mydict):
                #if it's alread in dict return the value
                return mydict[node]
            #if not add it to the dict
            mydict[node] = Node(node.val)
            #loop through the neigbors and append them to the neifbor of clone
            for nei in node.neighbors:
                #this will return the neigbors as node clones and append to this ode neigbors
                mydict[node].neighbors.append(dfs(nei))
            return mydict[node]
        dfs(node)
        return mydict[node]
        
    