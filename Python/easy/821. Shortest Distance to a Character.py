class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        c_index = []
        c_index_length = 0
        length = len(S)
        
        for i in range(length):
            if S[i] == C:
                c_index.append(i)
                c_index_length += 1
        
        res = []
        c = 0
        for i in range(length):
            if S[i] == C and i != c_index[c]:
                c += 1
                res.append(0)
            else:
                if c == c_index_length - 1:
                    res.append(max(i - c_index[c], c_index[c] - i))
                else:
                    res.append(min(max(i - c_index[c], c_index[c] - i),
                                   max(i - c_index[c + 1], c_index[c + 1] - i)))
        return res
                
        