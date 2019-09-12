class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a, b = a.strip('i').split('+'), b.strip('i').split('+')
        num_a = [int(x) for x in a]
        num_b = [int(x) for x in b]
        res_a = num_a[0]*num_b[0] - num_a[1]*num_b[1]
        res_b = num_a[0]*num_b[1] + num_a[1]*num_b[0]
        return str(res_a) + '+' + str(res_b) + 'i'
        
        