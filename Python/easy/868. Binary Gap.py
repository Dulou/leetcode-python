class Solution:
    def binaryGap(self, N: int) -> int:
        dis = -32
        res = 0
        while N > 0:
            if N & 1:
                if dis > res:
                    res = dis
                dis = 1
            else:
                dis += 1
            N = N >> 1
        return res
        