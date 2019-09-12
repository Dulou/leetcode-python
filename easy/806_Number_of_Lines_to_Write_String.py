class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        line = 0
        last = 0
        for s in S:
            last += widths[ord(s)-ord('a')]
            if last > 100:
                last = widths[ord(s)-ord('a')]
                line += 1
        return [line + 1, last]