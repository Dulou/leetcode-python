class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        a, b = a.split('+'), b.split('+')
        
        a1, a2 = int(a[0]), int(b[0])
        b1, b2 = int(a[1][:-1]), int(b[1][:-1])
        
        res_a = a1 * a2 - b1 * b2
        res_b = a1 * b2 + a2 * b1
        
        return str(res_a) + '+' + str(res_b) + 'i'
        