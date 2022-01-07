class Solution(object):
    '''
    This function works basically by going up the matrix from the bottom left and then going right
    when the row is 0. right = True.
    Then theres a while loop that goes down to the right one as long as it's inbound
    appends that value and coordinate to a list. 
    then sorts said list and replaces the actual coordinate in the matrix with the sorted value
    '''
    def diagonalSort(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(mat), len(mat[0])
        diags = n+m-1
        start=[m-1, 0]
        right=False
        for i in range(diags):
            keeper=start[:]
            if(i==m-1):
                right=True
            unsorted_list=[]
            coords=[]
            while start[0]>=0 and start[0]<=m-1 and start[1]>=0 and start[1]<=n-1:
                unsorted_list.append(mat[start[0]][start[1]])
                coords.append([start[0],start[1]])
                start[0]+=1
                start[1]+=1
            unsorted_list.sort()
            for i in range(len(unsorted_list)):
                mat[coords[i][0]][coords[i][1]]=unsorted_list[i]
                
            start=keeper
            if(not right):
                start[0]-=1
            else:
                start[1]+=1
        return mat

        '''
        A matrix diagonal is a diagonal line of cells starting from some cell in either the topmost row or leftmost column and going in the bottom-right direction until reaching the matrix's end. For example, the matrix diagonal starting from mat[2][0], where mat is a 6 x 3 matrix, includes cells mat[2][0], mat[3][1], and mat[4][2].

Given an m x n matrix mat of integers, sort each matrix diagonal in ascending order and return the resulting matrix.

 

Example 1:


Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]'''