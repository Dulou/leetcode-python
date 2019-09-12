import math
class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1:  # consider num < 0
            return False

        sum = 1
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                sum += (i + num / i)
                print sum

        return True if sum == num else False

if __name__ == "__main__":
    q = Solution()
    num = input()
    print q.checkPerfectNumber(num)