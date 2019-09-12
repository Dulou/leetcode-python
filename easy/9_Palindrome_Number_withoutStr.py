class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        tmp = x
        reverse = 0
        while tmp > 0:
            reverse = reverse * 10 + tmp % 10
            tmp /= 10
        return True if reverse == x else False

if __name__ == "__main__":
    line = raw_input()
    a = Solution()
    while line:
        x = int(line)
        print a.isPalindrome(x)
        line = raw_input()