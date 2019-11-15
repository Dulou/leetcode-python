class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        l = s.split(' ')
        
        for item in l:
            res.append(item[::-1])
        return ' '.join(res)
        