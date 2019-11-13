class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        num = x ^ y
        res = 0
        while num:
            res += num & 1
            num = num >> 1
        return res
            
        