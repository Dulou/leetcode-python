class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = 1e6
        while left < right:
            mid = int((left + right) // 2)
            if sum([(i-1) // mid + 1 for i in nums]) > threshold:
                left = mid + 1
            else:
                right = mid
        return right
            