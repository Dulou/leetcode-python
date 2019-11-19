class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        row = len(nums)
        col = len(nums[0])
        if row * col != r * c:
            return nums
        
        res = [[0 for i in range(c)] for j in range(r)]
        
        cn = 0
        rn = 0
        for i in range(row):
            for j in range(col):
                res[rn][cn] = nums[i][j]
                cn += 1
                if cn == c:
                    rn += 1
                    cn = 0
        return res
                
        