class Solution(object):
    def reachableNodes(self, n, edges, restricted):
        """
        :type n: int
        :type edges: List[List[int]]
        :type restricted: List[int]
        :rtype: int
        """
        graph = dict()
        restricted = {i:True for i in restricted}

        for x,y in edges:
            if(graph.get(x, "na") == "na"):
                graph[x] = [y]
            else:
                graph[x].append(y)
            
            if(graph.get(y, "na") == "na"):
                graph[y]=[x]
            else:
                graph[y].append(x)
        
        queue = []
        queue.append(0)
        count = 0
        visited = {i:False for i in range(len(edges)+1)}
        while queue:
            cur = queue.pop(0)
            count+=1
            visited[cur]=True
            for node in graph[cur]:
                if(visited[node]==False and restricted.get(node, False)==False):
                    visited[node]=True
                    queue.append(node)
        return count


        '''
        NOTE: USING SET INSTEAD OF A DICTIONARY FOR THE VISITED OBJECTS WILL RESULT IN TIMOUT ERROR. Still technically 'works' but will not pass LC checks because of time reasons
        2368. Reachable Nodes With Restrictions
Medium
427
17
Companies

There is an undirected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.

You are given a 2D integer array edges of length n - 1 where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree. You are also given an integer array restricted which represents restricted nodes.

Return the maximum number of nodes you can reach from node 0 without visiting a restricted node.

Note that node 0 will not be a restricted node.

 

Example 1:

Input: n = 7, edges = [[0,1],[1,2],[3,1],[4,0],[0,5],[5,6]], restricted = [4,5]
Output: 4
Explanation: The diagram above shows the tree.
We have that [0,1,2,3] are the only nodes that can be reached from node 0 without visiting a restricted node.

        
        '''