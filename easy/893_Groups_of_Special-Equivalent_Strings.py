class Solution(object):
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        s = set()
        for a in A:
            s.add(''.join(sorted(a[0::2])) + ''.join(sorted(a[1::2])))
        return len(s)