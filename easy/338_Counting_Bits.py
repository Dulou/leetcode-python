class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num == 0:
            return [0]
        res = [0 for i in range(num+1)]
        power_2 = []
        tmp = 1
        while tmp <= num:
            power_2.append(tmp)
            res[tmp] = 1
            tmp *= 2
        power_2.append(tmp)
        for i in range(len(power_2)-1):
            for j in range(power_2[i], power_2[i+1]):
                res[j] = 1 + res[j-power_2[i]]
                if j == num:
                    return res

"""
simpler and more elegant solution
"""
class Solution2(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = [0]
        while len(res) < num+1:
            res += [i+1 for i in res]
        return res[:num+1]