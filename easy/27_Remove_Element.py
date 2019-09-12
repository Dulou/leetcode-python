class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        #和26题类似，testcase的验证方式相同，排除和val值相同的项，返回长度length，并且调整nums的前length项
        index = 0
        for i in nums:
            if i == val:
                continue
            else:
                nums[index] = i
                index += 1
        return index