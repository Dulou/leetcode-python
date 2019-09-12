# -*- coding: utf-8 -*-
class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """

        #返回字符串中连续三个或以上相同字符的起始和结束位置
        res = []
        S += '-'         #解决S=aaa的问题，在后面加入一个字符
        length = len(S)
        if(length<1):
            return res
        char = S[0]
        begin_pos = 0
        end_pos = 0
        for i in xrange(length):
            if S[i]==char:
                continue
            else:
                end_pos = i-1
                if end_pos-begin_pos >= 2:
                    res.append([begin_pos,end_pos])
                begin_pos = i
                char = S[i]
        return res

if __name__ == "__main__":
    S = raw_input()
    a = Solution()
    while S:
        print a.largeGroupPositions(S)
        S = raw_input()
