class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        length = len(nums)
        width = len(nums[0])
        if r * c != length * width or (r == length and c == width):
            return nums
        
        res = []
        i,j = 0, 0
        for _ in range(r):
            tmp = []
            for _ in range(c):
                tmp.append(nums[i][j])
                j += 1
                if j == width:
                    j = 0
                    i += 1
            res.append(tmp)
        return res