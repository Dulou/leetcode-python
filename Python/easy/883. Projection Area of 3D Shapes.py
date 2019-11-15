class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        left = sum([max(l) for l in grid])
        bottom = sum([sum([int(item != 0) for item in l]) for l in grid])
        
        front = 0
        for i in range(len(grid[0])):
            tmp = [l[i] for l in grid]
            front += max(tmp)
        return left + bottom + front
        
        