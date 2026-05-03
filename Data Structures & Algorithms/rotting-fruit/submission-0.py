class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row,col=len(grid),len(grid[0])
        fresh=0
        q=deque()
        def fruitcheck(r,c):
            nonlocal fresh
            if(r<0 or c<0 or r>=row or c>=col or grid[r][c]==2 or grid[r][c]==0):
                return None
            grid[r][c]=2
            q.append([r,c])
            fresh-=1
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    fresh+=1
                if grid[i][j]==2:
                    q.append([i,j])
        time=0
        while fresh>0 and q:
            for i in range(len(q)):
                r,c=q.popleft()
                fruitcheck(r+1,c)
                fruitcheck(r-1,c)
                fruitcheck(r,c+1)
                fruitcheck(r,c-1)
            time+=1
        if fresh==0:
            return time
        else:
            return -1
                