class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        total=0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if(grid[i][j]==0):
                    continue
                #up
                if(i==0 or grid[i-1][j]==0):
                    total+=1
                #down
                if(i==len(grid)-1 or grid[i+1][j]==0):
                    total+=1
                #left
                if(j==0 or grid[i][j-1]==0):
                    total+=1
                if(j==len(grid[0])-1 or grid[i][j+1]==0):
                    total+=1
        return total

# You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

# The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

 

# Example 1:


# Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
# Output: 16
# Explanation: The perimeter is the 16 yellow stripes in the image above.
                