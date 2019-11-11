class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        res = 0
        
        row = [0] * n
        col = [0] * m
        
        for indice in indices:
            row[indice[0]] += 1
            col[indice[1]] += 1
        
        for i in range(n):
            for j in range(m):
               res += (row[i] + col[j]) % 2
        return res
        