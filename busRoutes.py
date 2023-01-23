class Solution(object):
    def numBusesToDestination(self, routes, source, target):
        """
        :type routes: List[List[int]]
        :type source: int
        :type target: int
        :rtype: int
        """
        if(source==target):
            return 0
        
        bfs = deque()
        visited_bus = set()
        visited_stops = set()
        graph = {}
        for i in range(len(routes)):
            for bus in routes[i]:
                if(graph.get(bus, "na") == "na"):
                    graph[bus] = [i]
                else:
                    graph[bus].append(i)
        bfs.append((source, 0))
        while bfs:
            stop, count = bfs.popleft()

            if(stop == target):
                return count
            for bus_number in graph[stop]:
                if(bus_number not in visited_bus):
                    visited_bus.add(bus_number)
                    for bstop in routes[bus_number]:
                        if(bstop not in visited_stops):
                            visited_stops.add(bstop)
                            bfs.append((bstop, count+1))
        return -1

        '''
        Labeled hard problem. Classic BFS approach with minor addition of having visited sets
        815. Bus Routes
Hard
2.8K
72
Companies

You are given an array routes representing bus routes where routes[i] is a bus route that the ith bus repeats forever.

    For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.

You will start at the bus stop source (You are not on any bus initially), and you want to go to the bus stop target. You can travel between bus stops by buses only.

Return the least number of buses you must take to travel from source to target. Return -1 if it is not possible.

 

Example 1:

Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 6
Output: 2
Explanation: The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.

Example 2:

Input: routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12
Output: -
        
        '''