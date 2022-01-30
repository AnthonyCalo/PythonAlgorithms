'''You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

 '''
 class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0 for _ in range(len(cost)+1)]

        for index in range(2, len(cost) + 1):
            dp[index] = min(cost[index-1]+dp[index-1], cost[index-2] + dp[index-2])
        return(dp[-1])
            
            
            
            
            
            