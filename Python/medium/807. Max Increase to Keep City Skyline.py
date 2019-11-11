class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        res = 0
        rowNum = len(grid)
        colNum = len(grid[0])
        
        rowSky = []
        for row in grid:
            rowSky.append(max(row))
        
        colSky = []
        for j in range(colNum):
            col = [grid[i][j] for i in range(rowNum)]
            colSky.append(max(col))
        
        for i in range(rowNum):
            for j in range(colNum):
                res += min(rowSky[i], colSky[j]) - grid[i][j]
        return res
        