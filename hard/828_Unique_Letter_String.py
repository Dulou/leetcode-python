class Solution(object):
    def uniqueLetterString(self, S):
        """
        :type S: str
        :rtype: int
        """

        # define UNIQ(S) as the number of unique characters in string S.
        # calculate the sum of UNIQ(substring) over all non-empty substrings of S
        # retrun the answer modulo 10 ^ 9 + 7.

        ## time limit exceed---due to python2.7's speed too low
        length = len(S)
        res = 0

        for i in xrange(length):
            dist = {}
            qq = 1
            for j in xrange(i, length):
                if S[j] not in dist:
                    dist[S[j]] = 1
                else:
                    dist[S[j]] += 1

                if (i == j):
                    res += 1
                else:
                    num = dist[S[j]] - 1
                    if (num == 0):
                        qq += 1
                    elif (num == 1):
                        qq -= 1

                    res += qq

        return res % 1000000007


if __name__ == "__main__":
    S = raw_input()
    a = Solution()
    while S:
        print a.uniqueLetterString(S)
        S = raw_input()