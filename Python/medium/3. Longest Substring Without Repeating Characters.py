class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        length = len(s)
        store = {}
    
        start = 0
        for i in range(length):
            if s[i] not in store:
                store[s[i]] = i
            else:
                if store[s[i]] >= start:
                    if i - start > res:
                        res = i - start
                    start = store[s[i]] + 1
                store[s[i]] = i
        
        return max(res, length - start)
        