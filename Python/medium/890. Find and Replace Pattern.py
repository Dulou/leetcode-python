class Solution:
    def match(self, word: str, pattern: str, length: int):
        pat = {}
        exist = {}
        for i in range(length):
            if pattern[i] not in pat:
                if word[i] in exist:
                    return False
                else:
                    pat[pattern[i]] = word[i]
                    exist[word[i]] = 0
            else:
                if word[i] != pat[pattern[i]]:
                    return False
        return True
            
        
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        length = len(pattern)
        
        res = []
        for word in words:
            if self.match(word, pattern, length):
                res.append(word)
        return res
        