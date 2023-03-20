class Solution(object):
    def maxJump(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        if(len(stones) in  [2,3]):
            return stones[-1] - stones[0]
        
        mj = 0
        for i in range(len(stones)-2):
            jump = stones[i +2] - stones[i]
            mj = max(mj, jump)
            
        return mj
    
'''
2498. Frog Jump II
Medium
344
59
Companies

You are given a 0-indexed integer array stones sorted in strictly increasing order representing the positions of stones in a river.

A frog, initially on the first stone, wants to travel to the last stone and then return to the first stone. However, it can jump to any stone at most once.

The length of a jump is the absolute difference between the position of the stone the frog is currently on and the position of the stone to which the frog jumps.

    More formally, if the frog is at stones[i] and is jumping to stones[j], the length of the jump is |stones[i] - stones[j]|.

The cost of a path is the maximum length of a jump among all jumps in the path.

Return the minimum cost of a path for the frog.
'''
        