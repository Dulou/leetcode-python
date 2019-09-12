class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for line in A:
            line.reverse()
            for i in range(len(line)):
                line[i] = int(line[i]==0)
        return A

if __name__ == "__main__":
    q = Solution()
    A = [[1,1,0],[1,0,1],[0,0,0]]
    print(q.flipAndInvertImage(A))