class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        dict = {}
        for t in T:
            dict[t] = dict.get(t, 0) + 1
        
        res = ''
        for s in S:
            res += s*dict.get(s, 0)
            dict[s] = -1
        
        for s, num in dict.items():
            if num > 0:
                res += s*num
        
        return res