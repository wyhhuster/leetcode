class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1)+len(s2)!=len(s3):
            return False
        dp=[[False]*(len(s2)+1) for _ in range(len(s1)+1)]
        dp[0][0]=True
        for i in range(1,len(s1)+1):
            if s1[i-1]==s3[i-1]:
                dp[i][0]=dp[i-1][0]
        for i in range(1,len(s2)+1):
            if s2[i-1]==s3[i-1]:
                dp[0][i]=dp[0][i-1]
        for i in range(1,len(s1)+1):
            for j in range(1,len(s2)+1):
                dp[i][j]= (dp[i-1][j] and s1[i-1]==s3[i+j-1]) or (dp[i][j-1] and s2[j-1]==s3[i+j-1])
        return dp[len(s2)][len(s1)]
A=Solution()
print(A.isInterleave(s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"))