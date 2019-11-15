class Solution:
    def calPoints(self, ops: List[str]) -> int:
        point = []
        for op in ops:
            if op == 'C':
                point.pop()
            elif op == 'D':
                point.append(point[-1] * 2)
            elif op == '+':
                point.append(point[-1] + point[-2])
            else:
                point.append(int(op))
        return sum(point)
        