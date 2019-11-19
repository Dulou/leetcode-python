class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            l = str(x)[1:]
        else:
            l = str(x)
        
        l = l[::-1]
        for i in range(len(l)):
            if l[i] != '0':
                l = l[i:]
                break
        
        res = int('-'+l) if x < 0 else int(l)
        if res > 2**31 - 1 or res < -2**31:
            return 0
        return res
        