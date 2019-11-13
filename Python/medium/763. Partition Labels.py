class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        length = len(S)
        last_index = {}
        for i in range(length):
            last_index[S[i]] = i
        
        res = []
        begin = end = 0
        
        for i in range(length):
            if last_index[S[i]] > end:
                end = last_index[S[i]]
            if i == end:
                res.append(end - begin + 1)
                begin = i + 1
        return res