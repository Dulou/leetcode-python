class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
        for i in range(3):
            row[i] = set(row[i])
        
        res = []
        for word in words:
            tmp = set(word.lower())
            for i in row:
                if tmp.issubset(i):
                    res.append(word)
                    break
        return res