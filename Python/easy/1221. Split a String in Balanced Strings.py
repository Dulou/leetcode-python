class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l = 0
        r = 0
        res = 0
        for item in s:
            if item == 'L':
                l += 1
            else:
                r += 1
            if l == r:
                res += 1
                l = 0
                r = 0
        return res
        