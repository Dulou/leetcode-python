class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        alphabet = {
            'q': 1, 'w': 1, 'e': 1, 'r': 1, 't': 1, 'y': 1, 'u': 1,
            'i': 1, 'o': 1, 'p': 1, 'a': 2, 's': 2, 'd': 2, 'f': 2,
            'g': 2, 'h': 2, 'j': 2, 'k': 2, 'l': 2, 'z': 3, 'x': 3,
            'c': 3, 'v': 3, 'b': 3, 'n': 3, 'm': 3,
        }
        
        res = []
        
        for word in words:
            index = alphabet[word[0].lower()]
            flag = False
            
            for w in word.lower():
                if alphabet[w] != index:
                    flag = True
                    break
            if flag:
                continue
            res.append(word)
        return res
            
            
            