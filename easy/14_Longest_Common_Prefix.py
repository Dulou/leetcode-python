class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ''
        if len(strs) == 1:
            return strs[0]

        prefix = ''
        length = len(strs[0])
        for i in xrange(length):
            for j in strs[1:]:
                if i >= len(j) or j[i] != strs[0][i]:
                    return prefix
            prefix += strs[0][i]
        return prefix

if __name__ == "__main__":
    line = input()
    a = Solution()
    while line:
        print a.longestCommonPrefix(line)
        line = input()