class Solution(object):
    def convert(self, s, numRows):
        if( numRows<=1):
            return s
        res=[[] for i in range(numRows)]
        #createa  matrix with length number of rows
        step=-1
        row=0
        #add char in s to res[row] then increment row by step
        #if row = 0 or the bottom row in matrix(numRows-1) reverse the step by times equalling negative 1
        for j in s:
            res[row]+=j
            if(row==0 or row==numRows-1):
                step*=-1
            row+=step
        for i in range(numRows):
            res[i]="".join(res[i])
        return "".join(res)
            