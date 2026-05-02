class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        row_count=[0]*row
        col_count=[0]*col
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    row_count[i]+=1
                    col_count[j]+=1
        res=0
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1 and (row_count[i]>1 or col_count[j]>1):
                    res+=1
        return res
