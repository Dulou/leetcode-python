class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        length = len(citations)
        record = [0 for i in range(length + 1)]
        for i in citations:
            if i > length:
                record[length] += 1
            else:
                record[i] += 1

        sum = 0
        for i in range(length, -1, -1):
            sum += record[i]
            if sum >= i:
                return i
        return 0