class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        if not S:
            return []
        
        res = []
        length = len(S)
        start = 0
        
        for i in range(length):
            if S[i] != S[start]:
                if i - start >= 3:
                    res.append([start, i - 1])
                start = i
            elif i == length - 1:
                if i - start >= 2:
                    res.append([start, i])
        return res
                
        