class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        
        length = len(strs[0])
        for i in range(length):
            sig = strs[0][i]
            for s in strs:
                try:
                    if s[i] != sig:
                        return strs[0][:i]
                except:
                    return strs[0][:i]
        return strs[0]
        