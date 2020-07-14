class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        for i in range(len(triangle)-2,-1,-1):
            for j in range(len(triangle[i])):
                triangle[i][j]=min(triangle[i+1][j],triangle[i+1][j+1])+triangle[i][j]
        return triangle[0][0]


    def minimumTotal1(self, triangle):
        dp=[triangle[-1][i] for i in range(len(triangle[-1]))]
        for i in range(len(triangle)-2,-1,-1):
            for j in range(0,i+1):
                dp[j]=min(dp[j],dp[j+1])+triangle[i][j]
            print(dp)
        return dp[0]
A=Solution()
print(A.minimumTotal([
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]))
print(A.minimumTotal1([
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]))