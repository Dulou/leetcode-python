class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        
        for num in nums:
            i = num if num > 0 else -num
            if nums[i - 1] < 0:
                res.append(i)
            else:
                nums[i - 1] *= -1
        return res
        