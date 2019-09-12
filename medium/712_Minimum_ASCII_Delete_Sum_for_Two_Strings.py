class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """

        # dp[i][j]表示s2的前i个字母和s1的前j个字母满足要求的最小ASCII和

        len_s1, len_s2 = len(s1), len(s2)
        dp = [[0 for j in range(len_s1+1)] for i in range(len_s2+1)]
        for j in range(1, len_s1+1):
            dp[0][j] = dp[0][j-1] + ord(s1[j-1])
        for i in range(1, len_s2+1):
            dp[i][0] = dp[i-1][0] + ord(s2[i-1])
        for i in range(1,len_s2+1):
            for j in range(1,len_s1+1):
                if s1[j-1] == s2[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j]+ord(s2[i-1]), dp[i][j-1]+ord(s1[j-1]))
        return dp[len_s2][len_s1]

if __name__ == "__main__":
    f = raw_input()
    b = raw_input()
    a = Solution()
    print (a.minimumDeleteSum(f,b))
