class Solution(object):
    def flipgame(self, fronts, backs):
        """
        :type fronts: List[int]
        :type backs: List[int]
        :rtype: int
        """
        #主要思路是任何一个数都能出现在后端，只有前后相同的数才不可能只出现在后端而不出现在前端
        length = len(fronts)
        front_equal_back = {}
        for i in xrange(length):
            if fronts[i] == backs[i]:
                #不能记录i，可能出现前后不等但是取值和之前的前后相等值相同的情况
                front_equal_back[fronts[i]] = 0

        min_num = 2000
        for i in xrange(length):
            if fronts[i] not in front_equal_back:
                if (fronts[i] < min_num):
                    min_num = fronts[i]
            if backs[i] not in front_equal_back:
                if (backs[i] < min_num):
                    min_num = backs[i]

        #没有符合要求的返回0
        return min_num if min_num != 2001 else 0

if __name__ == "__main__":
    f = input()
    b = input()
    a = Solution()
    while f:
        print a.flipgame(f,b)
        f = raw_input()
        b = raw_input()