class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        maxSum = nums[0]
        
        tmp = 0
        for i in range(len(nums)):
            tmp += nums[i]
            if tmp > maxSum:
                maxSum = tmp
            if tmp < 0:
                tmp = 0
        return maxSum
        