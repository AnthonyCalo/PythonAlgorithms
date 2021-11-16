class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        shift_char=0
        newmatrix=[]
        for k in range(len(matrix)):
            newmatrix_row=[]
            for i, j in enumerate(matrix[::-1]):
                newmatrix_row.append(j[shift_char])
            shift_char+=1
            newmatrix.append(newmatrix_row)
        for i in range(len(matrix)):
            matrix[i]=newmatrix[i]
        return (matrix)
            