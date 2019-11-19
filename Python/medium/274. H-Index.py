class Solution:
    def hIndex(self, citations: List[int]) -> int:
        res = 0
        citations.sort(reverse=True)
        
        for i in range(len(citations)):
            if citations[i] >= i + 1:
                res += 1
            else:
                break
        return res
        