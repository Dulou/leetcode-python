class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def isSelfDividingNumber(n):
            tmp = n
            while tmp > 0:
                q = tmp % 10
                tmp /= 10
                if q == 0 or n % q != 0:
                    return False
            return True
        
        res = []
        for i in range(left, right+1):
            if isSelfDividingNumber(i):
                res.append(i)
        return res