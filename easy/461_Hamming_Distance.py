class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        p = x^y
        res = 0
        while p!=0:
            res += p%2
            p /= 2
        return res