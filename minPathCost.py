class Solution(object):
    def minPathCost(self, grid, moveCost):
        """
        :type grid: List[List[int]]
        :type moveCost: List[List[int]]
        :rtype: int
        """
        m,n = len(grid), len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        def get_min_path(upRow, col):
            mc = 999999
            for column in range(n):
                cost = dp[upRow][column] + moveCost[grid[upRow][column]][col] 
                if(cost < mc):
                    mc = cost
            return mc

        def dfs(row):
            if(row == m):
                return
            for i in range(n):
                if(row == 0):
                    dp[row][i] = grid[row][i]
                else:
                    dp[row][i] = get_min_path(row-1, i) + grid[row][i]
          
            dfs(row+1)
        dfs(0)
        return min(dp[m-1])
    '''

Problem List
Premium
0
DCC Badge
2304. Minimum Path Cost in a Grid
Medium
641
97
Companies

You are given a 0-indexed m x n integer matrix grid consisting of distinct integers from 0 to m * n - 1. You can move in this matrix from a cell to any other cell in the next row. That is, if you are in cell (x, y) such that x < m - 1, you can move to any of the cells (x + 1, 0), (x + 1, 1), ..., (x + 1, n - 1). Note that it is not possible to move from cells in the last row.

Each possible move has a cost given by a 0-indexed 2D array moveCost of size (m * n) x n, where moveCost[i][j] is the cost of moving from a cell with value i to a cell in column j of the next row. The cost of moving from cells in the last row of grid can be ignored.

The cost of a path in grid is the sum of all values of cells visited plus the sum of costs of all the moves made. Return the minimum cost of a path that starts from any cell in the first row and ends at any cell in the last row.

 

Example 1:
    
    '''