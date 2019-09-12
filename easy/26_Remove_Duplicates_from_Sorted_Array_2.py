class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #返回删除后的长度，因为nums是引用，可以被外部查看
        #由于testcase查看nums的方式，可以不对nums数组进行删除操作，节省了时间复杂度
        if nums == []:
            return 0
        num = nums[0]
        index = 1
        flag = 1
        for i in nums:
            if flag == 1:
                flag = 0
                continue
            if i == num:
                continue
            nums[index] = i
            num = i
            index += 1
        return index

if __name__ == "__main__":
    f = input()
    a = Solution()
    while f:
        print a.removeDuplicates(f)
        print f
        f = input()
