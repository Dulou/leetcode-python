class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        res = 0
        distance = -32  #防止100000这种
        while N > 0:
            if N % 2 == 1:
                if distance > res:
                    res = distance
                distance = 0
            distance += 1
            N = N >> 1
        
        return res