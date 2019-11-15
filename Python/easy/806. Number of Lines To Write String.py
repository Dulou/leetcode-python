class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        if S == '':
            return [0, 0]
        line = 1
        width = 0
        
        for s in S:
            index = ord(s) - ord('a')
            width += widths[index]
            if width > 100:
                line += 1
                width = widths[index]
        return [line, width]
        