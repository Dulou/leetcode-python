class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        res = [0 for i in range(len(A))]
        even, odd = 0, 1
        for i in A:
            if i%2:
                res[odd] = i
                odd += 2
            else:
                res[even] = i
                even += 2
        return res