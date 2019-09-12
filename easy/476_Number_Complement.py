class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        tmp = 1
        while num > tmp:
            tmp = (tmp + 1) * 2 - 1
        return tmp - num