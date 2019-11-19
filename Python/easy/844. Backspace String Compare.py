class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s = []
        len_s = 0
        for item in S:
            if item == '#':
                if len_s > 0:
                    s.pop()
                    len_s -= 1
            else:
                s.append(item)
                len_s += 1
        
        t = []
        len_t = 0
        for item in T:
            if item == '#':
                 if len_t > 0:
                    t.pop()
                    len_t -= 1
            else:
                t.append(item)
                len_t += 1
        
        return ''.join(s) == ''.join(t)
        