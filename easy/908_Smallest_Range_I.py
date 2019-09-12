class Solution(object):
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        max_A, min_A = max(A), min(A)
        if max_A - K <= min_A + K:
            return 0
        else:
            return max_A - min_A - 2*K
        
"""
Simplest solution: return max(0, max_A - min_A - 2*K)
"""

"""
解析：数组变化后，最小值最大为min+K，最大值最小为max-A，此时差距最小
但需要注意的是，由于是变化后最大值与最小值的差距，这个差距不可能小于0
当min+K>max-K时，所有值都可以变化成单一相同值，差距为0
"""