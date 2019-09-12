# -*- coding: utf-8 -*-
class Solution(object):
    def maskPII(self, S):
        """
        :type S: str
        :rtype: str
        """

        res = ''
        if (ord(S[0])>=ord('a') and ord(S[0])<=ord('z')) or (ord(S[0])>=ord('A') and ord(S[0])<=ord('Z')):
            index = S.index('@')
            begin,end = S[0],S[index-1]
            if (ord(begin)>=ord('A') and ord(begin)<=ord('Z')):
                begin = chr(ord(begin)-ord('A')+ord('a'))
            if (ord(end)>=ord('A') and ord(end)<=ord('Z')):
                end = chr(ord(end)-ord('A')+ord('a'))
            res += begin+'*****'+end+'@'

            for i in xrange(index+1,len(S)):
                tmp = S[i]
                if (ord(tmp) >= ord('A') and ord(tmp) <= ord('Z')):
                    tmp = chr(ord(tmp) - ord('A') + ord('a'))
                res += tmp

            return res
        else:
            tmp = ''
            for i in xrange(len(S)):
                if S[i] in ['+', '-', '(', ')', ' ']:
                    continue
                tmp += S[i]
            length = len(tmp)
            if length > 10:
                res += '+'+'*'*(length-10)+'-***-***-'+tmp[-4:]
            else:
                res += '***-***-'+tmp[-4:]
            return res


if __name__ == "__main__":
    S = raw_input()
    a = Solution()
    while S:
        print a.maskPII(S)
        S = raw_input()
