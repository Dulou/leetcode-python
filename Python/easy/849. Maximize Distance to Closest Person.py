class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        res = 0
        
        loc = 0
        first = -1
        for i in range(len(seats)):
            if seats[i] == 1:
                if first == -1:
                    first = i
                    loc = i
                    continue
                if (i - loc) // 2 > res:
                    res = (i - loc) // 2
                loc = i
        
        if len(seats) - 1 - loc > res:
            res = len(seats) - 1 - loc
        if first > res:
            res = first
        return res
        