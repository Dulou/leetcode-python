class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        store = {}
        for word in A.split(' ') + B.split(' '):
            store[word] = store.get(word, 0) + 1     
        
        res = []
        for key in store.keys():
            if store[key] == 1:
                res.append(key)
        return res