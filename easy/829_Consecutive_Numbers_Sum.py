import math
class Solution(object):
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        #返回连加等于N的式子的个数
        #k * (2 * i + k - 1) = 2 * N
        end = int(math.sqrt(2*N))
        res = 0
        for k in xrange(1,end+1):
            if (2*N % k)==0:
                if ((2*N / k)+1-k)%2==0:
                    res += 1
        return res

if __name__ == "__main__":
    S = input()
    a = Solution()
    while S:
        print a.consecutiveNumbersSum(S)
        S = input()