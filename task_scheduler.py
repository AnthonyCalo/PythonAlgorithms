class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        if(n==0):
            return len(tasks)
        sd = dict()
        for i in tasks:
            sd[i] = sd.get(i,0)+1
        cycle=n+ 1
        res=0
        heap = []
        for v in sd.values():
            heapq.heappush(heap, -v)
        
        while heap:
            tmp = []
            count = 0
            for i in range(cycle):
                if(heap):
                    cur = heapq.heappop(heap)
                    count+=1
                    if(cur + 1 <0):
                        tmp.append(cur+1)
            if(tmp or heap):
                res+=cycle
                for val in tmp:
                    heapq.heappush(heap, val)
            else:
                res += count
                return res
        return res


        '''
        621. Task Scheduler
Medium
7.9K
1.6K
Companies

Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks.

 

Example 1:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: 
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.

Example 2:
        '''