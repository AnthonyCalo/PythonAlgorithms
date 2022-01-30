class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if(obstacleGrid[0][0]==1):
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        print(m, n)
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0]=1
        for row in range(m):
            for col in range(n):
                if(obstacleGrid[row][col]==1):
                    dp[row][col]==0
                    continue
                if(row == 0):
                    if(col==0):
                        continue
                    dp[row][col]=dp[row][col-1]
                elif col == 0:
                    if(row==0):
                        continue
                    dp[row][col]=dp[row-1][col]
                else:
                    dp[row][col] = dp[row-1][col] + dp[row][col-1]
                    
        return(dp[m-1][n-1])