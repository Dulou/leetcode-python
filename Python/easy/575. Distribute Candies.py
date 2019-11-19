class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        length = len(candies)
        
        kinds = 0
        store = {}
        for c in candies:
            if c not in store:
                kinds += 1
                store[c] = 0
        return min(kinds, length // 2)
        