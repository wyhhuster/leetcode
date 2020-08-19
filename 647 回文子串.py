class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=0
        dp=[[0]*len(s) for _ in range(len(s))]
        for i in range(len(s)-1,-1,-1):
            dp[i][i]=1
            count+=1
            for j in range(i+1,len(s)):
                if s[i]==s[j] and (j-i<3 or dp[i+1][j-1]):
                    dp[i][j]=1
                    if dp[i][j]==1:
                        count+=1
        return count
A=Solution()
print(A.countSubstrings("a"))
