class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for num in nums:
            if nums[abs(num) - 1] < 0:
                res.append(abs(num))
            else:
                nums[abs(num) - 1] *= -1
        return res

		
"""
这个解法满足无额外空间且时间复杂度为O(n)
思想为利用原数组进行标记，标记原则是若n出现，则使得nums[abs(num) - 1]*-1
但是这个解法没有直接使用字典所用时间短
"""
