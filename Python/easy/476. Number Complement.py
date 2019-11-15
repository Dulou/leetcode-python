class Solution:
    def findComplement(self, num: int) -> int:
        m = 2
        while num > m - 1:
            m *= 2
        return m - 1 - num
        