class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n=len(grid), len(grid[0])
        visited = []
        output=0
        def dfs(row, column):
            if(grid[row][column]=="0"):
                return
            if(grid[row][column]=="1" and [row, column] not in visited):
                visited.append([row,column])
            else:
                return
            up = [row-1, column]
            down = [row+1, column]
            left = [row, column-1]
            right = [row, column+1]
            neighbors=[up, down, left, right]
            for i in neighbors:
                if(i[0]<0 or i[1]<0 or i[0]>=m or i[1]>=n or i in visited):
                    continue
                else:
                    dfs(i[0],i[1])
        for row in range(len(grid)):
            for column in range(len(grid[row])):
                if([row, column] in visited or grid[row][column]=="0"):
                    continue
                if(grid[row][column]=="1"):
                    output+=1
                    dfs(row, column)
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