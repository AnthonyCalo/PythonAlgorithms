class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiag=set()
        negDiag=set()
        res=[]
        board = [["."]*n for i in range(n)]
        def backtracking(r):
            if(r==n):
                res.append(["".join(i) for i in board])
                return
            for c in range(n):
                if c in col or (c+r) in posDiag or (r-c)in negDiag:
                    continue
                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                board[r][c]="Q"
                backtracking(r+1)
                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c]="."

        backtracking(0)
        return res
'''
really fun problem. how to place queens on nxn board without them being able to attack each othr
'''