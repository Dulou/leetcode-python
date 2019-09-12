class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #返回删除后的长度，因为nums是引用，可以被外部查看
        if nums == []:
            return 0
        num = nums[0]
        i = 1
        while i<len(nums):
            if nums[i]==num:
                nums.remove(nums[i])
            else:
                num = nums[i]
                i += 1
        return len(nums)

if __name__ == "__main__":
    f = input()
    a = Solution()
    while f:
        print a.removeDuplicates(f)
        print f
        f = input()
