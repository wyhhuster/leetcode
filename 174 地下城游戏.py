class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        dp=[[0]*len(dungeon[0]) for i in range(len(dungeon))]

        for i in range(len(dungeon)-1,-1,-1):
            for j in range(len(dungeon[0])-1,-1,-1):
                if i==len(dungeon)-1 and j==len(dungeon[0])-1:
                    dp[i][j]=max(1,1-dungeon[i][j])
                elif i==len(dungeon)-1:
                    dp[i][j]=max(1,dp[i][j+1]-dungeon[i][j])
                elif j==len(dungeon[0])-1:
                    dp[i][j]=max(1,dp[i+1][j]-dungeon[i][j])
                else:
                    dp[i][j]=min(max(1,dp[i+1][j]-dungeon[i][j]),max(1,dp[i][j+1]-dungeon[i][j]))
        print(dp)
        return dp[0][0]
A=Solution()
print(A.calculateMinimumHP([[-2,-3,3],[-5,-10,1],[10,30,-5]]))