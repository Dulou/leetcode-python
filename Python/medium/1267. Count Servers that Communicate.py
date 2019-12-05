class Solution:
    def countServers(self, grid: List[List[int]]) -> int:       
        row = len(grid)
        col = len(grid[0])
        rowCount = [0 for i in range(row)]
        colCount = [0 for j in range(col)]
        
        res = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    rowCount[i] += 1
                    colCount[j] += 1
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 and (rowCount[i] > 1 or colCount[j] > 1):
                    res += 1
        return res
                    
        