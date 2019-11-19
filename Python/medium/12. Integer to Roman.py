class Solution:
    def intToRoman(self, num: int) -> str:
        cutoff = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        sig = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        res = ''
        
        i = 0
        while num > 0:
            if num >= cutoff[i]:
                res += sig[i]
                num -= cutoff[i]
            else:
                i += 1
        return res
        