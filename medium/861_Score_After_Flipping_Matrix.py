class Solution(object):
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        row, col = len(A), len(A[0])
        res_matrix = [row]
        for i in range(row):
            if not A[i][0]:
                A[i] = [int(A[i][j] == 0) for j in range(col)]
        for i in range(1, col):
            data = [A[j][i] for j in range(row)]
            if sum(data) <= row/2:
                res_matrix.append(row - sum(data))
            else:
                res_matrix.append(sum(data))
        res, mul = 0, 1
        for i in range(col):
            res += res_matrix[col-i-1]*mul
            mul *= 2
        return res