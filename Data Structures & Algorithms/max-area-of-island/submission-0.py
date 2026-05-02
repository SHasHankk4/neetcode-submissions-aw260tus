class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row,col=len(grid),len(grid[0])
        def dfs(r,c):
            if (r<0 or c<0 or r>=row or c>=col or grid[r][c]==0):
                return 0
            grid[r][c]=0
            return 1+dfs(r+1,c)+dfs(r-1,c)+dfs(r,c+1)+dfs(r,c-1)
        Max_area=0
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    area=dfs(i,j)
                    Max_area=max(Max_area,area)
        return Max_area