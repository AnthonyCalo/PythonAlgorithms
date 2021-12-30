class Solution:
    #solution is recursive fucnction. 
    #basically at each item in matrix if it is equal to 1 calls a function that turns every other item 
    # in that isalnd into a #. So for each isalnd it adds 1 to the num of islands
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n=len(grid), len(grid[0])
        output=0
        def dfs(row, column):
            if(row<0 or column<0 or row>=m or column>=n or grid[row][column]!="1"):
                return
            grid[row][column] = '#'
            dfs(row+1, column)
            dfs(row-1, column)
            dfs(row, column+1)
            dfs(row, column-1)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if( grid[i][j]=="1" ):
                    output+=1
                    dfs(i,j)
        return(output)
'''
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1'''