class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        res = []
        index = -1
        for s in ops:
            res.append(0)
            if s == "C":
                index -= 1
            elif s == 'D':
                index += 1
                res[index] = 2*res[index-1]
            elif s == '+':
                index += 1
                res[index] = res[index-1] + res[index-2]
            else:
                index += 1
                res[index] = int(s)
        return sum(res[:index+1])

"""
just use stack
"""
class Solution2(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        res = []
        for s in ops:
            if s == "C":
                res.pop()
            elif s == 'D':
                res.append(res[-1]*2)
            elif s == '+':
                res.append(res[-1]+res[-2])
            else:
                res.append(int(s))
        return sum(res)


if __name__ == "__main__":
    q = Solution()
    ops = ["36","28","70","65","C","+","33","-46","84","C"]
    print(q.calPoints(ops))