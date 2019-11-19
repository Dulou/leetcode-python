class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        str_nums = list(map(str, nums))
        maxlen = max(map(len, str_nums))
        str_nums.sort(reverse=True, key=lambda x: x * (maxlen // len(x) + 1))
        if str_nums[0] == '0':
            return '0'
        return ''.join(str_nums)