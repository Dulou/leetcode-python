class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        words_A = A.split()
        words_B = B.split()
        
        dict = {}
        for word in words_A:
            dict[word] = dict.get(word, 0) + 1
        for word in words_B:
            dict[word] = dict.get(word, 0) + 1
        
        res = []
        for word, num in dict.items():
            if num == 1:
                res.append(word)
                
        return res