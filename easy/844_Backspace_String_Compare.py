class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        res_s = ''
        res_t = ''
        for s in S:
            if s == '#':
                if res_s:
                    res_s = res_s[:-1]
            else:
                res_s += s
        for t in T:
            if t == '#':
                if res_t:
                    res_t = res_t[:-1]
            else:
                res_t += t
        return res_s == res_t