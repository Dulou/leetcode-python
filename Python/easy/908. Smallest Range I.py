class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        maxNum = max(A)
        minNum = min(A)
        return max(0, maxNum - minNum - 2 * K)
        