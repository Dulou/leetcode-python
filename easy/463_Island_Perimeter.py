class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        length = len(grid)
        width = len(grid[0])
        num1, renum1 = 0, 0
        for i in range(length):
            for j in range(width):
                if grid[i][j] == 1:
                    num1 += 1
                    if i > 0 and grid[i-1][j] == 1:
                        renum1 += 1
                    if j > 0 and grid[i][j-1] == 1:
                        renum1 += 1
                    if j < width-1 and grid[i][j+1] == 1:
                        renum1 += 1
                    if i < length-1 and grid[i+1][j] == 1:
                        renum1 += 1
        return num1*4 - renum1
		
"""
上下左右也有岛的时候将重复的边减去
"""