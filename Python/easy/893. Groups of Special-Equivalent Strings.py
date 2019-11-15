class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        s = set()
        for l in A:
            a = sorted(l[::2])
            b = sorted(l[1::2])
            s.add(''.join(a) + ''.join(b))
        return len(s)
        