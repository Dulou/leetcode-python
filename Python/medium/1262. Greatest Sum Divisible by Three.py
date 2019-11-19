class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        num_sum = sum(nums)
        if num_sum % 3 == 0:
            return num_sum
        elif num_sum % 3 == 1:
            min_1 = 10000
            min_2 = [10000, 10000]
            
            for num in nums:
                if num % 3 == 1 and num < min_1:
                    min_1 = num
                if num % 3 == 2:
                    if num < min_2[0]:
                        min_2[1] = min_2[0]
                        min_2[0] = num
                    elif num < min_2[1]:
                        min_2[1] = num
            return max(num_sum - min_1, num_sum - sum(min_2))
        else:
            min_2 = 10000
            min_1 = [10000, 10000]
            
            for num in nums:
                if num % 3 == 2 and num < min_2:
                    min_2 = num
                if num % 3 == 1:
                    if num < min_1[0]:
                        min_1[1] = min_1[0]
                        min_1[0] = num
                    elif num < min_1[1]:
                        min_1[1] = num
            return max(num_sum - min_2, num_sum - sum(min_1))