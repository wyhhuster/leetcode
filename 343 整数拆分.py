class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp=[0 for i in range(n+1)]
        dp[1]=1
        dp[2]=1
        for i in range(3,n+1):
            for j  in range(1,i//2+1):
                dp[i]=max(dp[i],j*(i-j),dp[j]*dp[i-j],j*dp[i-j],dp[j]*(i-j))
        return dp[n]
A=Solution()
print(A.integerBreak(10))
