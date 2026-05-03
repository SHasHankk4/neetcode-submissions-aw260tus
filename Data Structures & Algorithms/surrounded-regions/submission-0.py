class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row,col=len(board),len(board[0])
        q=deque()
        def bfs(r,c):
            if r<0 or r>=row or c<0 or c>=col or board[r][c]!="O":
                return None
            board[r][c]="T"
            q.append([r,c])
        for r in range(row):
            for c in range(col):
                if(r==0 or r==row-1 or c==0 or c==col-1)and board[r][c]=="O":
                    q.append([r,c])
                
        while q:
            for i in range(len(q)):
                r,c=q.popleft()  
                if board[r][c]=="O":
                    board[r][c]="T"
                bfs(r-1,c)
                bfs(r+1,c)
                bfs(r,c-1)
                bfs(r,c+1)
        for i in range(row):
            for j in range(col):
                if board[i][j]=="O":
                    board[i][j]="X"
                elif board[i][j]=="T":
                    board[i][j]="O"



        