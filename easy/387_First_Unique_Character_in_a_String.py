class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {}
        for i in s:
            if i not in dict:
                dict[i] = 0
            dict[i] += 1

        for i in range(len(s)):
            if dict[s[i]] == 1:
                return i
        return -1

"""
second solution
"""
class Solution2(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters = "abcdefghijklmnopqrstuvwxyz"
        index = [s.index(i) for i in letters if s.count(i) == 1]
        return min(index) if len(index) > 0 else -1