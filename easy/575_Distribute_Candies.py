class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        tmp = len(set(candies))
        return min(tmp, len(candies)/2)