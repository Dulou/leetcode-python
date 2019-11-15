class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        
        res = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    num = 4
                    if i - 1 >= 0 and grid[i-1][j] == 1:
                        num -= 1
                    if j - 1 >= 0 and grid[i][j-1] == 1:
                        num -= 1
                    if i + 1 < row and grid[i+1][j] == 1:
                        num -= 1
                    if j + 1 < col and grid[i][j+1] == 1:
                        num -= 1
                    res += num
        return res
        