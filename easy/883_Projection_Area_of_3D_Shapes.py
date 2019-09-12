class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        scale = len(grid)
        xy, xz, yz = 0, 0, 0
        for i in range(scale):
            xz += max(grid[i])
            tmp = 0
            for j in range(scale):
                xy += int(grid[i][j] != 0)
                if grid[j][i] > tmp:
                    tmp = grid[j][i]
            yz += tmp
        return xy + xz + yz