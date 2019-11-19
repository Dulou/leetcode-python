class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = [[i, nums[i]] for i in range(len(nums))]
        nums.sort(key=lambda x:x[1])
        left = 0
        right = len(nums) - 1
        while nums[left][1] + nums[right][1] != target:
            if nums[left][1] + nums[right][1] > target:
                right -= 1
            else:
                left += 1
        return [nums[left][0], nums[right][0]]
        