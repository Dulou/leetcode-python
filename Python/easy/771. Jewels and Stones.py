class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        store = {}
        res = 0
        for s in J:
            store[s] = 0
        for s in S:
            if s in store:
                res += 1
        return res
        