class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if(row[0]>target):
                return False
            if(target in row):
                return True
        return False

        '''74. Search a 2D Matrix
Medium

5205

234

Add to List

Share
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
 '''