class Solution(object):
    #递归
    def __init__(self):
        self.count=0
    def find(self,obstacleGrid,i,j):
        if not obstacleGrid[i][j] and i==len(obstacleGrid)-1 and j==len(obstacleGrid[0])-1:
            self.count+=1
            return
        if obstacleGrid[i][j]:
            return
        else:
            obstacleGrid[i][j] = 1
            if j+1<len(obstacleGrid[0]):
                self.find(obstacleGrid,i,j+1)
            if i+1<len(obstacleGrid):
                self.find(obstacleGrid,i+1,j)
            obstacleGrid[i][j]=0
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        self.find(obstacleGrid,0,0)
        return self.count
    #动态规划  压缩空间
    def uniquePathsWithObstacles1(self,obstacleGrid):
        dp=[0 for i in range(len(obstacleGrid[0]))]
        if obstacleGrid[0][0]==0:
            dp[0]=1
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j]==1:
                    dp[j]=0
                    continue
                if j-1>=0 and obstacleGrid[i][j-1]==0:
                    dp[j]+=dp[j-1]
        return dp[len(obstacleGrid[0])-1]
    #动态规划 不压缩空间
    def uniquePathsWithObstacles2(self,obstacleGrid):
        dp=[[0]*len(obstacleGrid[0]) for i in range(len(obstacleGrid))]
        if obstacleGrid[0][0]==0:
            dp[0][0]=1
        for i in range(1,len(obstacleGrid)):
            if obstacleGrid[i][0] or dp[i-1][0]==0:
                dp[i][0]=0
            else:
                dp[i][0]=1
        for i in range(1,len(obstacleGrid[0])):
            if obstacleGrid[0][i] or dp[0][i-1]==0:
                dp[0][i]=0
            else:
                dp[0][i]=1
        for i in range(1,len(obstacleGrid)):
            for j in range(1,len(obstacleGrid[0])):
                if obstacleGrid[i][j]==1:
                    dp[i][j]=0
                else:
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[len(obstacleGrid)-1][len(obstacleGrid[0])-1]



A=Solution()
print(A.uniquePathsWithObstacles2([[1]]))
