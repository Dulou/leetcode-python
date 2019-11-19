class Solution:
    def romanToInt(self, s: str) -> int:
        store = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }
        
        res = 0
        length = len(s)
        for i in range(length):
            if s[i] == 'I' and i + 1 < length and (s[i+1] == 'V' or s[i+1] == 'X'):
                res -= store[s[i]]
            elif s[i] == 'X' and i + 1 < length and (s[i+1] == 'L' or s[i+1] == 'C'):
                res -= store[s[i]]
            elif s[i] == 'C' and i + 1 < length and (s[i+1] == 'D' or s[i+1] == 'M'):
                res -= store[s[i]]
            else:
                res += store[s[i]]
        return res