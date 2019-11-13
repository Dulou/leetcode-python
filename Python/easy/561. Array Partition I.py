class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        length = len(nums)
        nums.sort()
        
        res = 0
        for i in range(0, length, 2):
            res += nums[i]
        return res
        