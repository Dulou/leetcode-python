class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        store = {}
        for s in chars:
            store[s] = store.get(s, 0) + 1
        
        res = 0
        for word in words:
            tmp = {}
            flag = 0
            for s in word:
                if s not in store:
                    flag = 1
                    break
                tmp[s] = tmp.get(s, 0) + 1
                if tmp[s] > store[s]:
                    flag = 1
                    break
            if flag:
                continue
            res += len(word)
        return res
            