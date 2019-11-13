class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        row = len(A)
        col = len(A[0])
        
        res = []
        for i in range(row):
            res.append([])
            for j in range(col):
                num = A
                res[i].append(int(A[i][col - j - 1] == 0))
        return res
        