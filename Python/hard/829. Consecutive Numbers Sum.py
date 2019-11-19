class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        res = 0
        n = 1
        while N >= n * (n + 1) / 2:
            if (N * 2 - n * (n - 1)) % (2 * n) == 0:
                res += 1
            n += 1
        return res