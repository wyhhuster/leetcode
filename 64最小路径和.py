class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        for i in range(len(grid[0])-2,-1,-1):
            grid[-1][i]=grid[-1][i+1]+grid[-1][i]
        for i in range(len(grid)-2,-1,-1):
            grid[i][-1]+=grid[i+1][-1]
        for i in range(len(grid)-2,-1,-1):
            for j in range(len(grid[0])-2,-1,-1):
                grid[i][j]=min(grid[i+1][j],grid[i][j+1])+grid[i][j]
        return grid[0][0]
A=Solution()
print(A.minPathSum([
  [1,3,1],
  [1,5,1],
  [4,2,1]
]))