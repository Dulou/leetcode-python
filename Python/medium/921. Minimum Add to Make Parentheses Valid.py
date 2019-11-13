class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        res = 0
        left = 0
        for s in S:
            if s == '(':
                left += 1
            elif left == 0:
                res += 1
            else:
                left -= 1
        return res + left
        