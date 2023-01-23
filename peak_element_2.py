class Solution(object):
    def findPeakGrid(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        visited = set()
        output = []
        def lessHelper(x, y, last):
            if(x<0 or x>len(mat)-1 or y<0 or y>len(mat[0])-1):
                return True
            
            res = (mat[x][y]<last)
            if(res):
                visited.add((x,y))
            return res
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                lst = mat[row][col]
                if((row,col) not in visited and lessHelper(row+1, col, lst) and lessHelper(row-1, col, lst) and lessHelper(row, col+1, lst)and lessHelper(row, col-1, lst)):
                    return [row, col]

'''
1901. Find a Peak Element II

A peak element in a 2D grid is an element that is strictly greater than all of its adjacent neighbors to the left, right, top, and bottom.

Given a 0-indexed m x n matrix mat where no two adjacent cells are equal, find any peak element mat[i][j] and return the length 2 array [i,j].

You may assume that the entire matrix is surrounded by an outer perimeter with the value -1 in each cell.

You must write an algorithm that runs in O(m log(n)) or O(n log(m)) time.

'''