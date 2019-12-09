class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod = 1
        sum_res = 0
        while n > 0:
            tmp = n % 10
            prod *= tmp
            sum_res += tmp
            n = n // 10
        return prod - sum_res
        