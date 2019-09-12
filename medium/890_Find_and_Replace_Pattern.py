class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        def match(word, pattern):
            dict = {}
            for x,y in zip(word, pattern):
                if dict.setdefault(x, y) != y:
                    return False
            return len(set(dict.values())) == len(dict)
        
        res = []
        for word in words:
            if match(word, pattern):
                res.append(word)
        return res