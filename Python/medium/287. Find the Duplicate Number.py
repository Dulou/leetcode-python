class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            item = -num if num < 0 else num
            if nums[item] < 0:
                return item
            else:
                nums[item] *= -1
            
        