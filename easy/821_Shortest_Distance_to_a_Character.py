class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        # 记录出现C的位置，然后对该位置左右分别形成距离
        index = []
        length = len(S)
        for i in xrange(length):
            if S[i] == C:
                index.append(i)

        result = [0 for i in xrange(length)]
        last_middle = 0
        index_len = len(index)
        for i in xrange(index_len - 1):
            middle = (index[i] + index[i + 1]) / 2
            for j in xrange(last_middle, index[i]):
                result[j] = index[i] - j
            for j in xrange(index[i] + 1, middle + 1):
                result[j] = j - index[i]
            last_middle = middle + 1
        if (index_len >=1):
            for j in xrange(last_middle, index[index_len - 1]):
                result[j] = index[index_len - 1] - j
            for j in xrange(index[index_len - 1] + 1, length):
                result[j] = j - index[index_len - 1]
        return result

if __name__ == "__main__":
    S = raw_input()
    C = raw_input()
    a = Solution()
    while S:
        print a.shortestToChar(S,C)
        S = raw_input()
        C = raw_input()