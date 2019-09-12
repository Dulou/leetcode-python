class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        size, length = len(A[0]), len(A)
        res = []
        for i in range(size):
            res.append([A[j][i] for j in range(length)])
        return res

"""
Simplest solution: return list(zip(*A))
"""