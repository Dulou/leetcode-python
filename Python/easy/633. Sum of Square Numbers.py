class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, int(c**0.5)
        while left <= right:
            tmp = left * left + right * right
            if tmp == c:
                return True
            elif tmp < c:
                left += 1
            else:
                right -= 1
        return False
        