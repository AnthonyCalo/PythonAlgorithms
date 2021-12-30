class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [0 for i in range(len(triangle)+1)]
        
        for i in triangle[::-1]:
            for j in range(len(i)):
                dp[j]= i[j] + min(dp[j], dp[j+1])
        return dp[0]
        