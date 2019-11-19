class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        import math
        if num <= 1:
            return False
        res = 0
        for i in range(2, math.ceil(math.sqrt(num))):
            if num % i == 0:
                res += i
                if num != i * i:
                    res += num // i
        return num == res + 1
        