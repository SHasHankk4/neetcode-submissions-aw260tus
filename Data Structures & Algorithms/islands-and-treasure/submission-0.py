class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row,col=len(grid),len(grid[0])
        visited=set()
        q=deque()
        def addRoom(r,c):
            if(r<0 or c<0 or r>=row or c>=col or (r,c) in visited or  grid[r][c]==-1):
                return None
            visited.add((r,c))
            q.append([r,c])
        
        for i in range(row):
            for j in range(col):
                if grid[i][j]==0:
                    q.append([i,j])
                    visited.add((i,j))
        dist_from_treasure=0

        while q:
            for i in range(len(q)):
                r,c=q.popleft()
                grid[r][c]=dist_from_treasure
                addRoom(r+1,c)
                addRoom(r-1,c)
                addRoom(r,c+1)
                addRoom(r,c-1)
            dist_from_treasure+=1