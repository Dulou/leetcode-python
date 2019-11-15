class Solution:
    def customSortString(self, S: str, T: str) -> str:
        count = dict()
        for s in T:
            count[s] = count.get(s, 0) + 1
        
        res = ''
        for s in S:
            if s in count:
                res += s * count[s]
                del count[s]
        
        for s in count:
            res += count[s] * s
        return res
        