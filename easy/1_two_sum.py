class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        tmp = nums[:]
        nums.sort()
        print target
        left = 0
        right = len(nums) - 1
        while (nums[left] + nums[right] != target):
            print left,right
            print nums[left] + nums[right]
            if (nums[left] + nums[right]) > target:
                print 1
                right -= 1
            else:
                print 2
                left += 1
        return [tmp.index(nums[left]), tmp.index(nums[right])]
if __name__ == "__main__":
    f = input()
    t = int(raw_input())
    a = Solution()
    while f:
        print a.twoSum(f,t)
        f = input()
        t = int(raw_input())