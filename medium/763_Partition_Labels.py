class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        res = []
        dict = {}
        for i in range(len(S)):
            dict[S[i]] = i
        label = 0
        start = 0
        for i in range(len(S)):
            if label < dict[S[i]]:
                label = dict[S[i]]
            if label == dict[S[i]] and i == label:
                res.append(label - start + 1)
                start = label + 1
        return res
        