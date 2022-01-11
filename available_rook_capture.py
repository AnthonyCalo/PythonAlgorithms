class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        m, n = len(board), len(board[0])

        for i in range(m):
            for j in range(n):
                if(board[i][j]=="R"):
                    rs = [i,j]
                    break
        print(rs)
        def dfs(x,y,direction):
            if(y<0 or y>n-1 or x<0 or x>m-1):
                return 0
            if(board[x][y]=="B"):
                return 0
            elif(board[x][y]=="p"):
                return 1
            
            if(direction=="L"):
                return dfs(x-1,y, "L")
            elif(direction=="R"):
                return dfs(x+1,y, "R")
            elif(direction=="U"):
                return dfs(x,y+1, "U")
            else:
                return dfs(x,y-1, "D")
        res = 0
        res+=(dfs(rs[0],rs[1], "L"))
        res+=(dfs(rs[0],rs[1], "R"))
        res+=(dfs(rs[0],rs[1], "U"))
        res+=(dfs(rs[0],rs[1], "D"))

        return res
            '''
            On an 8 x 8 chessboard, there is exactly one white rook 'R' and some number of white bishops 'B', black pawns 'p', and empty squares '.'.

When the rook moves, it chooses one of four cardinal directions (north, east, south, or west), then moves in that direction until it chooses to stop, reaches the edge of the board, captures a black pawn, or is blocked by a white bishop. A rook is considered attacking a pawn if the rook can capture the pawn on the rook's turn. The number of available captures for the white rook is the number of pawns that the rook is attacking.

Return the number of available captures for the white rook.
            '''