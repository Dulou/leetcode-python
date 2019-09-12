class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        digit = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        length = len(s)
        sum = 0
        for i in xrange(length):
            cur = digit[s[i]]
            if s[i]=='I' and i<length-1:
                sum += cur if s[i+1]!='V' and s[i+1]!='X' else -cur
            elif s[i]=='X' and i<length-1:
                sum += cur if s[i+1]!='L' and s[i+1]!='C' else -cur
            elif s[i]=='C' and i<length-1:
                sum += cur if s[i+1]!='D' and s[i+1]!='M' else -cur
            else:
                sum += cur
        return sum

if __name__ == "__main__":
    line = raw_input()
    a = Solution()
    while line:
        print a.romanToInt(line)
        line = raw_input()